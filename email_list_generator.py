#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Email List Generator for Gmail Distribution
WARNING: This is for educational purposes only!
"""

import random
import json
import os
from datetime import datetime

class EmailListGenerator:
    def __init__(self):
        self.common_domains = [
            "gmail.com", "yahoo.com", "hotmail.com", "outlook.com",
            "company.com", "corporation.com", "enterprise.com",
            "university.edu", "college.edu", "school.edu",
            "gov", "government.com", "state.gov",
            "smallbusiness.com", "startup.com", "tech.com"
        ]
        
        self.common_names = [
            "john", "jane", "michael", "sarah", "david", "lisa",
            "robert", "jennifer", "william", "elizabeth", "james",
            "mary", "richard", "patricia", "charles", "linda",
            "thomas", "barbara", "christopher", "susan", "daniel",
            "jessica", "matthew", "sarah", "anthony", "karen",
            "mark", "nancy", "donald", "betty", "steven", "helen"
        ]
        
        self.corporate_titles = [
            "admin", "manager", "director", "ceo", "cto", "cfo",
            "hr", "it", "support", "sales", "marketing", "finance",
            "operations", "security", "compliance", "legal"
        ]
    
    def generate_corporate_emails(self, count=100):
        """Generate corporate email addresses"""
        emails = []
        
        corporate_domains = [
            "company.com", "corporation.com", "enterprise.com",
            "business.com", "firm.com", "group.com", "holdings.com"
        ]
        
        for i in range(count):
            name = random.choice(self.common_names)
            lastname = random.choice(self.common_names)
            domain = random.choice(corporate_domains)
            
            # Different email formats
            formats = [
                f"{name}.{lastname}@{domain}",
                f"{name}{lastname}@{domain}",
                f"{name[0]}{lastname}@{domain}",
                f"{name}@{domain}",
                f"{lastname}@{domain}"
            ]
            
            email = random.choice(formats)
            emails.append(email)
        
        return emails
    
    def generate_government_emails(self, count=50):
        """Generate government email addresses"""
        emails = []
        
        gov_domains = [
            "gov", "government.com", "state.gov", "federal.gov",
            "municipal.gov", "county.gov", "city.gov"
        ]
        
        for i in range(count):
            name = random.choice(self.common_names)
            lastname = random.choice(self.common_names)
            domain = random.choice(gov_domains)
            
            formats = [
                f"{name}.{lastname}@{domain}",
                f"{name}{lastname}@{domain}",
                f"{name[0]}{lastname}@{domain}"
            ]
            
            email = random.choice(formats)
            emails.append(email)
        
        return emails
    
    def generate_university_emails(self, count=75):
        """Generate university email addresses"""
        emails = []
        
        edu_domains = [
            "university.edu", "college.edu", "school.edu",
            "institute.edu", "academy.edu"
        ]
        
        for i in range(count):
            name = random.choice(self.common_names)
            lastname = random.choice(self.common_names)
            domain = random.choice(edu_domains)
            
            formats = [
                f"{name}.{lastname}@{domain}",
                f"{name}{lastname}@{domain}",
                f"{name[0]}{lastname}@{domain}",
                f"{name}@{domain}"
            ]
            
            email = random.choice(formats)
            emails.append(email)
        
        return emails
    
    def generate_general_emails(self, count=200):
        """Generate general email addresses"""
        emails = []
        
        general_domains = [
            "gmail.com", "yahoo.com", "hotmail.com", "outlook.com",
            "aol.com", "icloud.com", "protonmail.com"
        ]
        
        for i in range(count):
            name = random.choice(self.common_names)
            lastname = random.choice(self.common_names)
            domain = random.choice(general_domains)
            
            # Add numbers sometimes
            if random.random() < 0.3:
                number = random.randint(1, 999)
                formats = [
                    f"{name}.{lastname}{number}@{domain}",
                    f"{name}{lastname}{number}@{domain}",
                    f"{name[0]}{lastname}{number}@{domain}"
                ]
            else:
                formats = [
                    f"{name}.{lastname}@{domain}",
                    f"{name}{lastname}@{domain}",
                    f"{name[0]}{lastname}@{domain}",
                    f"{name}@{domain}"
                ]
            
            email = random.choice(formats)
            emails.append(email)
        
        return emails
    
    def generate_small_business_emails(self, count=50):
        """Generate small business email addresses"""
        emails = []
        
        business_domains = [
            "smallbusiness.com", "startup.com", "tech.com",
            "consulting.com", "services.com", "solutions.com"
        ]
        
        for i in range(count):
            name = random.choice(self.common_names)
            lastname = random.choice(self.common_names)
            domain = random.choice(business_domains)
            
            formats = [
                f"{name}.{lastname}@{domain}",
                f"{name}@{domain}",
                f"admin@{domain}",
                f"info@{domain}",
                f"contact@{domain}"
            ]
            
            email = random.choice(formats)
            emails.append(email)
        
        return emails
    
    def create_comprehensive_email_list(self, total_count=500):
        """Create comprehensive email list with all categories"""
        print("Generating comprehensive email list...")
        
        all_emails = []
        
        # Generate emails by category
        corporate_emails = self.generate_corporate_emails(int(total_count * 0.3))
        government_emails = self.generate_government_emails(int(total_count * 0.1))
        university_emails = self.generate_university_emails(int(total_count * 0.15))
        general_emails = self.generate_general_emails(int(total_count * 0.4))
        business_emails = self.generate_small_business_emails(int(total_count * 0.05))
        
        all_emails.extend(corporate_emails)
        all_emails.extend(government_emails)
        all_emails.extend(university_emails)
        all_emails.extend(general_emails)
        all_emails.extend(business_emails)
        
        # Remove duplicates
        all_emails = list(set(all_emails))
        
        # Shuffle the list
        random.shuffle(all_emails)
        
        return all_emails
    
    def save_email_lists(self, emails):
        """Save email lists to files"""
        # Save main list
        with open("target_emails.txt", 'w') as f:
            for email in emails:
                f.write(f"{email}\n")
        
        # Save categorized lists
        categories = {
            "corporate_emails.txt": [e for e in emails if any(domain in e for domain in ["company.com", "corporation.com", "enterprise.com"])],
            "government_emails.txt": [e for e in emails if any(domain in e for domain in ["gov", "government.com"])],
            "university_emails.txt": [e for e in emails if ".edu" in e],
            "general_emails.txt": [e for e in emails if any(domain in e for domain in ["gmail.com", "yahoo.com", "hotmail.com"])],
            "business_emails.txt": [e for e in emails if any(domain in e for domain in ["smallbusiness.com", "startup.com", "tech.com"])]
        }
        
        for filename, email_list in categories.items():
            with open(filename, 'w') as f:
                for email in email_list:
                    f.write(f"{email}\n")
        
        # Save statistics
        stats = {
            "generation_date": datetime.now().isoformat(),
            "total_emails": len(emails),
            "categories": {name: len(email_list) for name, email_list in categories.items()}
        }
        
        with open("email_list_stats.json", 'w') as f:
            json.dump(stats, f, indent=2)
        
        print(f"Saved {len(emails)} emails to target_emails.txt")
        print("Categorized lists saved:")
        for filename, email_list in categories.items():
            print(f"  {filename}: {len(email_list)} emails")
    
    def create_high_value_targets(self):
        """Create list of high-value targets"""
        high_value_emails = [
            # Corporate executives
            "ceo@company.com", "cto@company.com", "cfo@company.com",
            "president@corporation.com", "vice.president@enterprise.com",
            
            # Government officials
            "director@gov", "commissioner@gov", "secretary@gov",
            "administrator@government.com",
            
            # IT administrators
            "admin@company.com", "administrator@corporation.com",
            "it.admin@enterprise.com", "sysadmin@company.com",
            
            # Financial personnel
            "finance@company.com", "accounting@corporation.com",
            "treasurer@enterprise.com", "controller@company.com",
            
            # HR personnel
            "hr@company.com", "human.resources@corporation.com",
            "recruiting@enterprise.com", "personnel@company.com"
        ]
        
        with open("high_value_targets.txt", 'w') as f:
            for email in high_value_emails:
                f.write(f"{email}\n")
        
        print(f"Created high-value targets list: {len(high_value_emails)} emails")
    
    def create_industry_specific_lists(self):
        """Create industry-specific email lists"""
        industries = {
            "healthcare": ["hospital.com", "medical.com", "healthcare.com"],
            "finance": ["bank.com", "financial.com", "investment.com"],
            "technology": ["tech.com", "software.com", "it.com"],
            "education": ["university.edu", "college.edu", "school.edu"],
            "government": ["gov", "government.com", "state.gov"],
            "retail": ["store.com", "retail.com", "shop.com"],
            "manufacturing": ["manufacturing.com", "factory.com", "industrial.com"]
        }
        
        for industry, domains in industries.items():
            emails = []
            for domain in domains:
                for name in self.common_names[:10]:  # Use first 10 names
                    emails.append(f"{name}@{domain}")
                    emails.append(f"admin@{domain}")
                    emails.append(f"info@{domain}")
            
            filename = f"{industry}_emails.txt"
            with open(filename, 'w') as f:
                for email in emails:
                    f.write(f"{email}\n")
            
            print(f"Created {filename}: {len(emails)} emails")

def main():
    """Main execution function"""
    print("="*60)
    print("EMAIL LIST GENERATOR FOR GMAIL DISTRIBUTION")
    print("="*60)
    print("WARNING: This is for educational purposes only!")
    print("="*60)
    
    generator = EmailListGenerator()
    
    try:
        # Get user preferences
        total_count = int(input("Enter total number of emails to generate (default 500): ") or "500")
        
        print(f"\nGenerating {total_count} email addresses...")
        
        # Generate comprehensive email list
        emails = generator.create_comprehensive_email_list(total_count)
        
        # Save all lists
        generator.save_email_lists(emails)
        
        # Create high-value targets
        generator.create_high_value_targets()
        
        # Create industry-specific lists
        generator.create_industry_specific_lists()
        
        print("\n" + "="*60)
        print("EMAIL LIST GENERATION COMPLETED")
        print("="*60)
        print("Files created:")
        print("- target_emails.txt (main list)")
        print("- corporate_emails.txt")
        print("- government_emails.txt")
        print("- university_emails.txt")
        print("- general_emails.txt")
        print("- business_emails.txt")
        print("- high_value_targets.txt")
        print("- Industry-specific lists")
        print("- email_list_stats.json")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

