# Zapp Chat: Your AI-Powered WhatsApp Assistant for Small Businesses

Welcome to Zapp Chat, an AI-driven WhatsApp chatbot designed to empower small businesses like yours. Zapp Chat automates customer interactions, providing instant and precise responses to inquiries about your products, operating hours, and more. This allows you to focus on what truly matters – growing your business.

## Support Us

If you find this project helpful and would like to support future projects, consider buying us a coffee! Your support helps us continue building innovative AI solutions.

<a href="https://www.buymeacoffee.com/blazzmocompany"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=blazzmocompany&button_colour=40DCA5&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00"></a>

Your contributions go a long way in fueling our passion for creating intelligent and user-friendly applications.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Poetry Setup](#poetry-installation)
    - [Docker Setup](#docker-installation)
- [Learn More](#learn-more)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**Tired of juggling customer messages on WhatsApp while trying to run your business?**

Let Zapp Chat take the wheel!

**Zapp Chat is an AI-powered WhatsApp assistant built specifically for small businesses**. 

It's like having a tireless team member dedicated to providing instant, accurate responses to your customers 24/7.

No more missed messages, frustrated customers, or late-night scrambling. Zapp Chat handles it all – from answering product questions and sharing business hours to capturing leads and scheduling appointments. You get to focus on what you do best: growing your business.

## Features

* **Automated Customer Interactions:** Provides 24/7 availability and instant responses.
* **Multimodal Communication:**  Handles voice, media, and text seamlessly.
* **Business Information Retrieval:**  Delivers accurate information about your products, services, and more.
* **Lead Generation:**  Captures valuable customer data and identifies potential leads.
* **CRM Integration:**  Connects with your CRM system for enhanced customer management.
* **Analytics and Insights:** Tracks key performance indicators to optimize bot performance.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python (>= 3.10)
- Node.js and npm

### Installation

#### Poetry Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/blazzbyte/zappchat.git
   ```
   ```bash
   cd zappchat/
   ```
2. **Install Dependencies:**
   ```bash
   poetry install
   ```
3. **Start the Backend Server:**
   ```bash
   python main.py
   ```

#### Docker Installation
1. **Make sure you have Docker installed and running**
2. **Build the Docker image**
```bash
docker build -t zappchat .
```
3. Run the Docker container
```bash
docker run -p 8000:8000 zappchat 
```

(This maps port 8000 on your host machine to port 8000 in the container).
Now your Zapp Chat backend should be up and running!
## Learn More

To learn more about Zapp chat and its technologies, refer to the following resources:

-   [gemini vertes Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/overview)
-   [Supabase Documentation](https://supabase.com/docs)
-   [Whatsapp Documentation](https://business.whatsapp.com/developers/developer-hub)
- [Langchain Documentation](https://python.langchain.com/v0.2/docs/introduction/) - learn about Langchain (Python features).
- [Langchainjs Documentation](https://js.langchain.com/v0.2/docs/introduction/) - learn about Langchain (Javascript features).

## Contributing

Contributions to Alice are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with a clear commit message.
4.  Push your changes to your fork.
5.  Create a pull request to merge your changes into the main repository.

## License

Alice is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

Feel free to contribute, report issues, or suggest improvements to make Alice even better!