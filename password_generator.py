import random
import string
import hashlib
from datetime import datetime

class QuantumGenerator:
    def __init__(self):
        self.initialize_components()
        
    def initialize_components(self):
        # Character sets for password complexity
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?~`"
        self.numbers = string.digits
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        
        # Movie quotes and references (categorized by strength)
        self.epic_quotes = {
            100: [  # Ultimate strength quotes
                "IAmIronMan", "AvengersAssemble", "WakandaForever",
                "WithGreatPowerComesGreatResponsibility", "IAmBatman",
                "MayTheForceBeWithYou", "YouShallNotPass", "HereIsJohnny",
                "IAmTheOneWhoKnocks", "WinterIsComing", "DarkKnightRises",
                "ElementaryMyDearWatson", "ToInfinityAndBeyond", "HoustonWeHaveAProblem",
                "FranchiselyMyDearIDontGiveADamn", "IllMakeHimAnOfferHeCantRefuse",
                "TheresNoPlaceLikeHome", "ImKingOfTheWorld", "HereIsLookingAtYouKid",
                "MrStarkIDontFeelSoGood", "KeepYourFriendsCloseEnemiesCloser",
                "ThereCanBeOnlyOne", "DoOrDoNotThereIsNoTry", "TheForceIsStrongWithThis",
                "LukeSkywalkerIAmYourFather", "TheChosenOne", "NeverTellMeTheOdds"
                "Nirvan""iamnotdead" "Onyourleft"
            ],
            90: [   # Very strong quotes
                "ThisIsTheWay", "IAmYourFather", "IllBeBack",
                "HastaLaVistaBaby", "YippeeKiYay", "TheMatrixHasYou",
                "ForFrodo", "PerfectlyBalanced", "ThanosDemandsSilence",
                "IAmVengeance", "IAmTheNight", "WhyDoWeFall",
                "WhySoSerious", "LifeIsLikeABoxOfChocolates",
                "YouCantHandleTheTruth", "ImGonnaMakeHimAnOffer",
                "SayHelloToMyLittleFriend", "HereIsJohnnyShining",
                "TheNameIsBondJamesBond", "ShakeNotStirred",
                "TheresNoSpoonMatrix", "FollowTheWhiteRabbit",
                "WelcomeToTheDesertOfTheReal", "KnockKnockNeo"
            ],
            80: [   # Strong quotes
                "OnYourLeft", "ICanDoThisAllDay", "GrootIsGroot",
                "TonyStarkBuiltThisInACave", "ImAlwaysAngry",
                "TrustButVerify", "IAmTheOneWhoKnocks", "SayMyName",
                "WhatIsInTheBox", "GameOverMan", "GetToTheCopter",
                "IAmTheLaw", "ThisIsSparta", "TonightWeDineInHell",
                "TheyMayTakeOurLives", "FreedomBraveheart",
                "YouShallNotPassGandalf", "PreciousGollum",
                "MyPreciousRing", "OneRingToRuleThemAll"
            ],
            70: [   # Good quotes
                "HulkSmash", "WebHead", "ImBatman", "SuperMan",
                "UseTheForce", "JediMaster", "SithLord", "Excelsior",
                "GreatPowerGreatResponsibility", "FlyYouFools",
                "RunForestRun", "HoustonProblem", "BeamMeUpScotty",
                "LightspeedStarWars", "MayTheForceBeWithYou",
                "LiveLongAndProsper", "ItsAliveItsAlive",
                "ElementaryWatson", "TheBoyWhoLived", "Expelliarmus"
            ]
        }
        
        # Leet speak mappings (enhanced)
        self.leet_speak = {
            'a': ['4', '@', 'Д', '∆', '/\\'],
            'b': ['8', '6', 'ß', '฿', '|3'],
            'e': ['3', '€', '∑', '∈', '[-'],
            'g': ['6', '9', 'G', 'פ', '&'],
            'i': ['1', '!', '|', '¡', ']['],
            'l': ['1', '|', '£', '⅃', '[]_'],
            'o': ['0', 'Ø', '○', '◊', '()'],
            's': ['5', '$', '§', '∫', '§'],
            't': ['7', '+', '†', '┼', '-|-'],
            'z': ['2', 'ƶ', '≥', 'ᶾ', '≥']
        }
        
        # Common words for strength variation
        self.strength_words = {
            'high': ['quantum', 'cyber', 'neural', 'crypto', 'matrix', 'phoenix', 'omega',
                    'infinity', 'cosmic', 'stellar', 'nebula', 'galaxy', 'quantum', 'cipher',
                    'enigma', 'titan', 'dragon', 'phoenix', 'thunder', 'lightning'],
            'medium': ['secure', 'protect', 'shield', 'guard', 'defend', 'safety',
                      'fortress', 'castle', 'bastion', 'citadel', 'sentinel', 'warden'],
            'low': ['pass', 'word', 'code', 'key', 'lock', 'safe']
        }
        
    def generate_password(self, strength_level=100, use_quotes=True, use_leet=True):
        """Generate a password with specified strength level and options"""
        if strength_level < 1 or strength_level > 100:
            strength_level = 100
            
        # Base length based on strength
        base_length = max(12, int(strength_level / 5))
        
        password_parts = []
        
        # Start with a movie quote if enabled and strength is high enough
        if use_quotes and strength_level >= 70:
            # Get quotes for this strength level and above
            available_quotes = []
            for level, quotes in self.epic_quotes.items():
                if level <= strength_level:
                    available_quotes.extend(quotes)
            
            if available_quotes:
                # 10% chance to use multiple quotes for extra complexity
                if random.random() < 0.1:
                    num_quotes = random.randint(2, 3)
                    selected_quotes = random.sample(available_quotes, k=min(num_quotes, len(available_quotes)))
                    for quote in selected_quotes:
                        if random.random() < 0.3:  # 30% chance to split quote
                            parts = [quote[i:i+random.randint(3,5)] for i in range(0, len(quote), random.randint(3,5))]
                            password_parts.extend(parts)
                        else:
                            password_parts.append(quote)
                else:
                    quote = random.choice(available_quotes)
                    if random.random() < 0.3:  # 30% chance to split quote
                        parts = [quote[i:i+random.randint(3,5)] for i in range(0, len(quote), random.randint(3,5))]
                        password_parts.extend(parts)
                    else:
                        password_parts.append(quote)
        
        # Add strength words with variation
        if strength_level >= 80:
            words = random.sample(self.strength_words['high'], 
                               k=random.randint(1, 2))
        elif strength_level >= 50:
            words = random.sample(self.strength_words['medium'] + 
                               self.strength_words['high'],
                               k=random.randint(1, 2))
        else:
            words = random.sample(self.strength_words['low'] + 
                               self.strength_words['medium'],
                               k=random.randint(1, 2))
        password_parts.extend(words)
        
        # Add numbers based on strength
        num_count = max(2, int(strength_level / 15))
        numbers = []
        for _ in range(num_count):
            if random.random() < 0.3:  # Sometimes add year-like numbers
                numbers.append(str(random.randint(1970, 2030)))
            else:
                numbers.append(str(random.randint(0, 999)).zfill(random.randint(1, 3)))
        password_parts.extend(numbers)
        
        # Add special characters based on strength
        if strength_level > 30:
            special_count = max(2, int(strength_level / 20))
            specials = []
            for _ in range(special_count):
                if random.random() < 0.5:
                    # Add groups of similar specials
                    group = random.choice([
                        "!@#", "$%^", "&*()", "_+-=",
                        "[]{}","|;:", ",.<>?", "~`"
                    ])
                    specials.append(random.choice(group))
                else:
                    specials.append(random.choice(self.special_chars))
            password_parts.extend(specials)
        
        # Shuffle parts
        random.shuffle(password_parts)
        
        # Join parts with random separators if strength is high
        if strength_level >= 70 and random.random() < 0.7:
            separators = ['_', '.', '-', '@', '#', '$', '&']
            password = random.choice(separators).join(password_parts)
        else:
            password = ''.join(password_parts)
        
        # Apply leet speak transformations based on strength
        if use_leet and strength_level >= 60:
            password = self.apply_leet_speak(password, strength_level)
        
        # Add random characters to meet minimum length if needed
        while len(password) < base_length:
            char_set = self.lowercase + self.uppercase
            if strength_level > 30:
                char_set += self.special_chars
            if strength_level > 60:
                char_set += self.numbers
            password += random.choice(char_set)
        
        # Final complexity adjustments
        password = self.add_complexity(password, strength_level)
        
        # Ensure maximum length isn't excessive
        max_length = min(32, base_length + 10)
        if len(password) > max_length:
            # Try to cut at a separator if present
            separators = ['_', '.', '-', '@', '#', '$', '&']
            cut_points = [i for i in range(max_length-5, max_length)
                         if password[i] in separators]
            if cut_points:
                return password[:random.choice(cut_points)+1]
            return password[:max_length]
            
        return password
    
    def apply_leet_speak(self, text, strength):
        """Apply leet speak transformations based on strength"""
        result = ""
        for char in text:
            if char.lower() in self.leet_speak and random.random() < (strength / 150):
                result += random.choice(self.leet_speak[char.lower()])
            else:
                result += char
        return result
    
    def add_complexity(self, password, strength):
        """Add final complexity based on strength level"""
        parts = list(password)
        
        # Ensure at least one uppercase
        if not any(c.isupper() for c in parts):
            idx = random.randint(0, len(parts)-1)
            parts[idx] = parts[idx].upper()
        
        # Ensure at least one lowercase
        if not any(c.islower() for c in parts):
            idx = random.randint(0, len(parts)-1)
            parts[idx] = parts[idx].lower()
        
        # Ensure at least one number
        if not any(c.isdigit() for c in parts):
            parts.append(random.choice(self.numbers))
        
        # Ensure at least one special char for high strength
        if strength > 50 and not any(c in self.special_chars for c in parts):
            parts.append(random.choice(self.special_chars))
        
        # Final shuffle
        random.shuffle(parts)
        
        return ''.join(parts) 