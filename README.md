# 🧠 MySQL Database Assistant

A powerful LangChain-powered MySQL Assistant that leverages Groq's LLM to answer natural language questions about your database. Query, analyze, and explore your MySQL data effortlessly through an intuitive Streamlit web interface.

## ✨ Features

- **Natural Language Queries**: Ask questions about your database in plain English
- **Intelligent SQL Generation**: Automatically converts natural language to SQL queries
- **Interactive Web Interface**: Clean and user-friendly Streamlit dashboard
- **ReAct Agent Architecture**: Uses LangChain's ReAct framework for intelligent reasoning
- **Groq LLM Integration**: Powered by Llama-3.3-70B model for accurate responses
- **Real-time Processing**: Get instant answers to your database questions

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- MySQL database
- Groq API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SQL-Agent-
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy the `.env` file and add your Groq API key:
   ```bash
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```

4. **Configure database connection**
   - Edit `db.py` and add your MySQL connection details:
   ```python
   conn = mysql.connector.connect(
       host="your_host",
       user="your_username", 
       password="your_password",
       database="your_database_name"
   )
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
SQL-Agent-/
├── app.py              # Streamlit web interface
├── agent.py            # LangChain agent configuration
├── llm.py              # Groq LLM setup
├── db.py               # MySQL database connection
├── prompt.py           # ReAct prompt template
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
└── README.md          # Project documentation
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY = "your_groq_api_key"
```

### Database Setup

Update the connection parameters in `db.py`:

```python
conn = mysql.connector.connect(
    host="localhost",           # Your MySQL host
    user="your_username",       # Your MySQL username
    password="your_password",   # Your MySQL password
    database="your_database"    # Your database name
)
```

## 💡 Usage Examples

Once the application is running, you can ask questions like:

- "What are all the tables in this database?"
- "Show me the top 10 customers by revenue"
- "How many orders were placed last month?"
- "What's the average price of products in the electronics category?"
- "Find all users who haven't logged in for more than 30 days"

## 🛠 Technical Details

### Architecture

The application uses a **ReAct (Reasoning and Acting) agent** pattern:

1. **Question**: User inputs natural language query
2. **Thought**: Agent analyzes what information is needed
3. **Action**: Agent decides to query the database
4. **Action Input**: Agent generates appropriate SQL query
5. **Observation**: Agent receives query results
6. **Final Answer**: Agent formulates human-readable response

### Components

- **LangChain Agent**: Orchestrates the reasoning and action cycle
- **Groq LLM**: Provides natural language understanding and SQL generation
- **MySQL Connector**: Handles database interactions
- **Streamlit**: Provides the web interface

## 📦 Dependencies

- `streamlit` - Web application framework
- `langchain` - LLM application framework
- `langchain_groq` - Groq integration for LangChain
- `mysql-connector-python` - MySQL database connector
- `python-dotenv` - Environment variable management

## 🔒 Security Considerations

- **API Keys**: Keep your Groq API key secure and never commit it to version control
- **Database Access**: Use dedicated database users with minimal required permissions
- **Input Validation**: The agent includes built-in protections against SQL injection
- **Environment Variables**: Always use `.env` files for sensitive configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

**Connection Error**: 
- Verify MySQL server is running
- Check connection parameters in `db.py`
- Ensure database user has proper permissions

**API Error**:
- Verify your Groq API key is correct
- Check your Groq account has sufficient credits

**Import Error**:
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version compatibility

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with detailed information about your problem

---

