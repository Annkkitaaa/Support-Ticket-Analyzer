
 # Support Ticket Analyzer

A simple AI-powered tool that automatically analyzes customer support tickets using OpenAI's GPT-3.5 API. This tool helps categorize tickets, assign priority levels, and estimate resolution times.

## Features
- Automatic ticket categorization
- Priority level assignment
- Resolution time estimation
- Bulk ticket processing
- CSV export of results

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/support-ticket-analyzer.git
cd support-ticket-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

1. Simple ticket analysis:
```python
from analyzer import TicketAnalyzer

analyzer = TicketAnalyzer()
result = analyzer.analyze_ticket("I can't log into my account")
print(result)
```

2. Bulk analysis:
```python
from analyzer import TicketAnalyzer
from sample_tickets import SAMPLE_TICKETS

analyzer = TicketAnalyzer()
results = analyzer.analyze_bulk_tickets(SAMPLE_TICKETS)
print(results)
```

## Output Format
The analyzer provides results in the following format:
```json
{
    "category": "Technical/Billing/Account/Feature Request",
    "priority": "Low/Medium/High",
    "estimated_resolution_time": "hours",
    "ticket_text": "original ticket content"
}
```


