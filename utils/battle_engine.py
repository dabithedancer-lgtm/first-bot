import random

class BattleEngine:
    @staticmethod
    def simulate_raid(team_cards, boss_stats):
        """
        Simulates a party vs boss battle.
        team_cards: List of dicts {'name': str, 'atk': int, 'hp': int}
        boss_stats: Dict {'attack': int, 'health': int, 'speed': int}
        """
        logs = []
        boss_hp = boss_stats['health']
        boss_atk = boss_stats['attack']
        
        # Calculate Team Total HP
        team_hp = sum(c['hp'] for c in team_cards)
        
        turn = 0
        max_turns = 15
        
        while boss_hp > 0 and team_hp > 0 and turn < max_turns:
            turn += 1
            logs.append(f"**Turn {turn}**")
            
            # 1. Player Phase: All active cards attack
            total_dmg = 0
            details = []
            
            for card in team_cards:
                if card['hp'] <= 0: continue
                
                # Damage Variance (60% - 100%)
                variance = 0.6 + (random.random() * 0.4)
                dmg = int(card['atk'] * variance)
                
                # Crit (15% Chance, 1.5x Dmg)
                crit_text = ""
                if random.random() < 0.15:
                    dmg = int(dmg * 1.5)
                    crit_text = " **CRIT!**"
                
                total_dmg += dmg
                if crit_text: 
                    details.append(f"{card['name']}{crit_text}")

            boss_hp -= total_dmg
            
            # Log formatting
            hp_bar = "█" * int((boss_hp / boss_stats['health']) * 10)
            logs.append(f"Team dealt **{total_dmg:,}** dmg! Boss: `{hp_bar}` ({max(0, boss_hp):,})")
            if details:
                logs.append(f"Notable: {', '.join(details)}")

            if boss_hp <= 0: break

            # 2. Boss Phase
            # Boss deals damage to collective HP (simplified raid logic)
            boss_dmg = int(boss_atk * (0.8 + random.random() * 0.4))
            team_hp -= boss_dmg
            
            logs.append(f"👹 Boss attacked for **{boss_dmg:,}** damage!")

        win = boss_hp <= 0
        result_text = "🏆 **VICTORY**" if win else "💀 **DEFEAT**"
        logs.append(f"\n{result_text}")
        
        return { "win": win, "log": "\n".join(logs) }