# InsightFlow

## Social media performance analytics using AI 

This repository demonstrates a basic analytics module for analyzing social media engagement using **Langflow** and **DataStax Astra DB**. The project includes mock data, database integration, and workflow automation to calculate and provide insights on social media post performance.  

## Features  
- Simulated social media engagement data.  
- Database operations using DataStax Astra DB.  
- Workflow creation and analysis using Langflow.  
- Insight generation via GPT integration in Langflow
  
## Youtube Link
Below is the youtube link with our detailed project explaination <br>
https://youtu.be/YaHhHPXdKUE

## Project Files  

1. **`mock_engagement_data.csv`**  
   - A CSV file containing mock engagement data for various post types (e.g., carousel, reels, static images).  
   - Data columns include:
     - `Post_ID`: Unique identifier for each post.
     - `Post_Type`: Type of post (e.g., carousel, reel, static image).  
     - `Likes`: Number of likes.  
     - `Shares`: Number of shares.  
     - `Comments`: Number of comments.  

2. **`load_data_to_astradb.ipynb`**  
   - A Jupyter Notebook that:
     - Connects to your **DataStax Astra DB** instance.  
     - Loads the `mock_engagement_data.csv` into a table.    

3. **`FINAL_FLOW.json`**  
   - A Langflow JSON file that defines the workflow to:  
     1. Accept a user prompt. 
     2. Query DataStax Astra DB for average engagement metrics for the given prompt.  
     3. Generate insights using GPT integration.

### Prerequisites  
- **DataStax Astra DB** account and active database instance.  
- **Langflow** installed for workflow automation.  
- Python environment with Jupyter Notebook installed.  

### Steps  

#### 1. Load Engagement Data  
1. Open the Jupyter Notebook `load_data.ipynb`.  
2. Follow the steps to:  
   - Connect to your Astra DB instance.  
   - Load `mock_engagement_data.csv` into the database.  

#### 2. Use the Langflow Workflow  
1. Import the `FINAL_FLOW.json` file into Langflow.  
2. Configure the database connection in Langflow to point to your Astra DB instance.  
3. Run the workflow

## Tools and Technologies Used  
- **DataStax Astra DB**: Cloud-native database for managing the engagement data.  
- **Langflow**: No-code/low-code workflow creation for analysis and GPT integration.  
- **Python**: Used for loading the data into the database.

