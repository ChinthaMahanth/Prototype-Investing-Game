def quiz_game():
    print("Welcome to the Investment & Finance Quiz!")
    print("Answer the questions by typing the letter of the correct option.\n")
    
    score = 0
    
    questions = [
        {
            "question": "1. What does 'Buy and Hold' strategy involve?",
            "options": ["A. Selling stocks frequently", 
                        "B. Purchasing stocks and holding long-term", 
                        "C. Investing only in bonds", 
                        "D. Following daily news strictly"],
            "answer": "B"
        },
        {
            "question": "2. Dollar-Cost Averaging (DCA) helps investors:",
            "options": ["A. Reduce the impact of market volatility", 
                        "B. Predict stock prices", 
                        "C. Buy only growth stocks", 
                        "D. Avoid paying taxes"],
            "answer": "A"
        },
        {
            "question": "3. Value Investing is based on:",
            "options": ["A. Buying stocks with high growth potential", 
                        "B. Seeking undervalued stocks based on financial analysis", 
                        "C. Focusing only on dividends", 
                        "D. Following market news"],
            "answer": "B"
        },
        {
            "question": "4. Growth Investors primarily focus on:",
            "options": ["A. Companies with strong future growth potential", 
                        "B. Companies paying high dividends", 
                        "C. Bonds and fixed income", 
                        "D. Market indexes"],
            "answer": "A"
        },
        {
            "question": "5. Dividend Investing focuses on:",
            "options": ["A. Companies that reinvest all profits", 
                        "B. Stocks paying regular dividends", 
                        "C. Cryptocurrency", 
                        "D. Short-term trading"],
            "answer": "B"
        },
        {
            "question": "6. What is the purpose of Asset Allocation?",
            "options": ["A. Spread risk across different asset classes", 
                        "B. Focus on one stock only", 
                        "C. Avoid taxes", 
                        "D. Track daily news"],
            "answer": "A"
        },
        {
            "question": "7. Technical Analysis primarily studies:",
            "options": ["A. Company earnings reports", 
                        "B. Price and volume patterns", 
                        "C. Dividend history", 
                        "D. Economic policies"],
            "answer": "B"
        },
        {
            "question": "8. Personal finance fundamentals include:",
            "options": ["A. Building an emergency fund", 
                        "B. Paying off high-interest debts", 
                        "C. Creating a budget", 
                        "D. All of the above"],
            "answer": "D"
        },
        {
            "question": "9. A stock represents:",
            "options": ["A. Debt owed by the company", 
                        "B. Partial ownership in a company", 
                        "C. Government bond", 
                        "D. Cryptocurrency"],
            "answer": "B"
        },
        {
            "question": "10. Dividends are typically paid:",
            "options": ["A. Annually", "B. Quarterly", "C. Every week", "D. Only when stock price rises"],
            "answer": "B"
        },
        {
            "question": "11. What does the P/E ratio indicate?",
            "options": ["A. Profit per employee", 
                        "B. Price investors are willing to pay per earnings", 
                        "C. Total sales of a company", 
                        "D. Dividend growth"],
            "answer": "B"
        },
        {
            "question": "12. Good news about a company can lead to:",
            "options": ["A. Stock price decrease", 
                        "B. Buying pressure and price increase", 
                        "C. Bankruptcy", 
                        "D. No change in stock price"],
            "answer": "B"
        },
        {
            "question": "13. Central banks influence the economy by:",
            "options": ["A. Controlling interest rates and money supply", 
                        "B. Choosing stock market winners", 
                        "C. Paying dividends to investors", 
                        "D. Running companies directly"],
            "answer": "A"
        },
        {
            "question": "14. The NYSE is known for listing:",
            "options": ["A. Small startup companies", 
                        "B. Large, established companies (blue-chip stocks)", 
                        "C. Only tech companies", 
                        "D. Only foreign companies"],
            "answer": "B"
        },
        {
            "question": "15. What is Socially Responsible Investing (SRI)?",
            "options": ["A. Investing in companies based only on dividends", 
                        "B. Integrating ESG factors into investment decisions", 
                        "C. Short-term trading", 
                        "D. Ignoring company ethics"],
            "answer": "B"
        }
    ]
    
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").strip().upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")
    
    print(f"Quiz Over! Your score: {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent! You know your finance very well.")
    elif score >= len(questions)//2:
        print("Good job! Keep learning to improve.")
    else:
        print("Keep studying! Finance can be tricky, but you'll get there.")

quiz_game()
