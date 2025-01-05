import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import pandas as pd
from datetime import datetime

# Load environment variables
load_dotenv()

class TicketAnalyzer:
    def __init__(self):
        """Initialize the ticket analyzer with OpenAI API"""
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
    def analyze_ticket(self, ticket_text):
        """Analyze a single support ticket using GPT"""
        try:
            # Create prompt for analysis
            prompt = f"""Analyze this customer support ticket and provide:
            1. Category (Technical/Billing/Account/Feature Request)
            2. Priority (Low/Medium/High)
            3. Estimated resolution time in hours
            
            Provide response in JSON format.
            
            Ticket: {ticket_text}"""
            
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a customer support ticket analyzer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            
            # Parse and return the result
            result = json.loads(response.choices[0].message.content)
            result['ticket_text'] = ticket_text
            return result
            
        except Exception as e:
            print(f"Error analyzing ticket: {e}")
            return None
    
    def analyze_bulk_tickets(self, tickets):
        """Analyze multiple tickets and return as DataFrame"""
        results = []
        for ticket in tickets:
            analysis = self.analyze_ticket(ticket)
            if analysis:
                results.append(analysis)
        
        # Convert to DataFrame and save
        df = pd.DataFrame(results)
        filename = f"analysis_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")
        return df

def main():
    # Import sample tickets
    from sample_tickets import SAMPLE_TICKETS
    
    # Create analyzer instance
    analyzer = TicketAnalyzer()
    
    # Analyze all tickets
    results = analyzer.analyze_bulk_tickets(SAMPLE_TICKETS)
    
    # Print summary
    print("\nAnalysis Summary:")
    print(f"Total tickets analyzed: {len(results)}")
    print("\nCategory Distribution:")
    print(results['category'].value_counts())
    print("\nPriority Distribution:")
    print(results['priority'].value_counts())
    print("\nAverage Resolution Time:", results['estimated_resolution_time'].mean())

if __name__ == "__main__":
    main()