# **The Synergy App**  

The Synergy App is a cutting-edge tool designed to transcribe unstructured audio input and transform it into a logically organized, actionable report. Developed during the **OxAI Summer MVP Hackathon**, this project demonstrates the potential of AI-driven solutions for project organization and task management, using **custom actions** built on the **experimental AI JSON Framework** and **Whisper API**.  

## **Key Features**  
- **Custom Actions**: Tailor-made `get_transcription` and `report` actions, designed to leverage the flexibility of the AI JSON Framework.  
- **Audio Transcription**: Converts audio files into text using Whisper API for high accuracy.  
- **Unstructured to Structured Conversion**: Organizes rambling thoughts into a concise project report with sections like:  
  - Project Summary  
  - Timeline Overview  
  - Task Sequence  
  - Total Duration  
- **JSON Output**: Produces a JSON schema detailing tasks, durations, and logical execution order for easy integration.  

## **How It Works**  
1. **Audio Input**: Users provide an audio file (e.g., project discussions, brainstorming sessions).  
2. **Custom Transcription**: The `get_transcription` action processes the audio into text using Whisper API.  
3. **AI-Powered Report Creation**:  
   - The custom `report` action generates a coherent report from the raw transcription, organizing it into logical sections.  
4. **Task Structuring**: The `structure` action converts the report into a JSON schema containing tasks, durations, and execution order.  
5. **Output**: A JSON file summarizes the project for easy analysis or integration.  

## **Frameworks and APIs Used**  
- **AI JSON Framework**:  
  This project builds on the experimental AI JSON Framework with **custom actions** for transcription and report generation. Learn more about AI JSON [here](https://aijson.com/).  
- **Whisper API**:  
  Used for robust and accurate audio transcription, ensuring high-quality input data for report generation.  
- **LLM API (Claude-3)**:  
  Employs an advanced language model to generate structured reports and task organization.  

## **Code Overview**  
The Synergy App showcases how the AI JSON Framework can be extended with **custom actions**. Below is a breakdown of the custom logic:  

### **Custom Actions**  
- **`get_transcription`**:  
  - Retrieves audio input and converts it to text using Whisper API.  
  - Provides the foundation for subsequent report generation.  
- **`report`**:  
  - Analyzes transcription data and organizes it into sections: Project Summary, Timeline Overview, Task Sequence, and Total Duration.  

### **Structured Conversion (`structure`)**  
- Generates a JSON output schema with key fields for tasks, durations, and execution order.  

### **Example Output**  
```json  
{  
  "tasks": ["Define project goals", "Create MVP", "Test MVP"],  
  "durations": ["1 day", "2 days", "1 day"],  
  "order": [1, 2, 3]  
}  
```  

## **Getting Started**  

### **Prerequisites**  
- Python 3.9 or higher  
- API keys for:  
  - Whisper API  
  - LLM service (e.g., Claude-3)  
- Access to the AI JSON Framework  

### **Setup**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/synergy-app.git  
   cd synergy-app  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Configure API Keys:  
   - Add your Whisper API and LLM API keys to the configuration file or environment variables. Example:  
     ```bash  
     WHISPER_API_KEY="your-whisper-api-key"  
     LLM_API_KEY="your-llm-api-key"  
     ```  

4. Configure the AI JSON Framework:  
   - Ensure custom actions (`get_transcription` and `report`) are correctly integrated in the configuration.  

5. Run the app:  
   ```bash  
   python main.py  
   ```  

## **Contributing**  
We welcome contributions! If you’d like to enhance the Synergy App or adapt it for other use cases, feel free to open a pull request or raise an issue.  

## **License**  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

