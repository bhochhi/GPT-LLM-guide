graph TB
    Client(Web Interface)
    Streamlit(Streamlit)
    VertexAI(Vertex AI Studio)
    Gemini(Gemini Pro v1.5)
    ResponsibleAI(Responsible AI)
    Data(Custom Data)
    Model(Pre-trained Model)

    Client -- "Submit SEO request with context" --> Streamlit
    Streamlit -- "Facilitate request" --> VertexAI
    VertexAI -- "Leverage Gemini for analysis" --> Gemini
    Gemini -- "SEO analysis and recommendations" --> VertexAI
    VertexAI -- "Return recommendations" --> Streamlit
    Streamlit -- "Display recommendations" --> Client
    VertexAI -- "Model training with custom data" --> Data
    Data -- "Training and fine-tuning" --> Gemini
    VertexAI -- "Uses Pre-trained Model" --> Model
    VertexAI -- "Integrates" --> ResponsibleAI
    ResponsibleAI -- "Ensures ethical use and compliance" --> VertexAI

    style Streamlit fill:#4CAF50,stroke:#333,stroke-width:2px
    style VertexAI fill:#FF6F00,stroke:#333,stroke-width:2px
    style Gemini fill:#1E88E5,stroke:#333,stroke-width:2px
    style ResponsibleAI fill:#F44336,stroke:#333,stroke-width:2px
    style Data fill:#FFC107,stroke:#333,stroke-width:2px
    style Model fill:#9C27B0,stroke:#333,stroke-width:2px
    style Client fill:#0f9d58,stroke:#333,stroke-width:2px
