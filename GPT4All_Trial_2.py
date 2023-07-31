{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "machine_shape": "hm",
      "authorship_tag": "ABX9TyNngNxaSnqnMmFEDvn5ake7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sarazayan/ChatwithPDF/blob/main/GPT4All_Trial_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive/')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RRkWFAqHbBvu",
        "outputId": "dd9ac74e-7f8f-42cb-abf4-acb4da8b9b1c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive/; to attempt to forcibly remount, call drive.mount(\"/content/drive/\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls '/content/drive/MyDrive/Multiple_PDFs'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BPdme-mIb-ra",
        "outputId": "c5a16513-697a-4894-b44a-eb6d3fe451e4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2021_02_04_PR_Carbon_Neutrality_objectives.pdf\n",
            "Artificial_Intelligence_in_Business.pdf\n",
            "Mckinsey_HowAICanChangeyourBusiness.pdf\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x_4kW2nVUEdw",
        "outputId": "ca71c398-6c44-44d8-fe49-2c9e590080d4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "The following NEW packages will be installed:\n",
            "  poppler-utils\n",
            "0 upgraded, 1 newly installed, 0 to remove and 15 not upgraded.\n",
            "Need to get 174 kB of archives.\n",
            "After this operation, 754 kB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 poppler-utils amd64 0.86.1-0ubuntu1.1 [174 kB]\n",
            "Fetched 174 kB in 2s (114 kB/s)\n",
            "Selecting previously unselected package poppler-utils.\n",
            "(Reading database ... 123105 files and directories currently installed.)\n",
            "Preparing to unpack .../poppler-utils_0.86.1-0ubuntu1.1_amd64.deb ...\n",
            "Unpacking poppler-utils (0.86.1-0ubuntu1.1) ...\n",
            "Setting up poppler-utils (0.86.1-0ubuntu1.1) ...\n",
            "Processing triggers for man-db (2.9.1-1) ...\n"
          ]
        }
      ],
      "source": [
        "!apt-get install poppler-utils  #to present pages of p"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -Uqqq pip --progress-bar off\n",
        "!pip install -qqq langchain==0.0.173 --progress-bar off\n",
        "!pip install -qqq chromadb==0.3.23 --progress-bar off\n",
        "!pip install -qqq pypdf==3.8.1 --progress-bar off\n",
        "!pip install -qqq pygpt4all==1.1.0 --progress-bar off\n",
        "!pip install -qqq pdf2image==1.16.3 --progress-bar off"
      ],
      "metadata": {
        "id": "AG1q7Ha4Uaxz",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "114a1da3-ad1f-4024-cd12-79dfb346813c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\n",
            "\u001b[0m  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for hnswlib (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for sentence-transformers (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "google-colab 1.0.0 requires requests==2.27.1, but you have requests 2.31.0 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0m\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\n",
            "\u001b[0m\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\n",
            "\u001b[0m  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for pygpt4all (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\n",
            "\u001b[0m\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\n",
            "\u001b[0m"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#!gdown 1DpFisoGXsQbpQJvijuvxkLW_pg-FUUMF"
      ],
      "metadata": {
        "id": "A1103-RgUf4n"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!wget https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin #4GB_memory , 6B parameter"
      ],
      "metadata": {
        "id": "vgJxS1rtUiTj",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f5bc8fb9-9dfb-42b3-c172-a526067fae44"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2023-07-30 06:34:32--  https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin\n",
            "Resolving gpt4all.io (gpt4all.io)... 172.67.71.169, 104.26.0.159, 104.26.1.159, ...\n",
            "Connecting to gpt4all.io (gpt4all.io)|172.67.71.169|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 3785248281 (3.5G)\n",
            "Saving to: ‘ggml-gpt4all-j-v1.3-groovy.bin’\n",
            "\n",
            "ggml-gpt4all-j-v1.3  36%[======>             ]   1.30G  41.3MB/s    in 36s     \n",
            "\n",
            "2023-07-30 06:35:08 (37.0 MB/s) - Connection closed at byte 1394212864. Retrying.\n",
            "\n",
            "--2023-07-30 06:35:09--  (try: 2)  https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin\n",
            "Connecting to gpt4all.io (gpt4all.io)|172.67.71.169|:443... connected.\n",
            "HTTP request sent, awaiting response... 206 Partial Content\n",
            "Length: 3785248281 (3.5G), 2391035417 (2.2G) remaining\n",
            "Saving to: ‘ggml-gpt4all-j-v1.3-groovy.bin’\n",
            "\n",
            "ggml-gpt4all-j-v1.3 100%[+++++++============>]   3.52G  45.9MB/s    in 53s     \n",
            "\n",
            "2023-07-30 06:36:03 (42.7 MB/s) - ‘ggml-gpt4all-j-v1.3-groovy.bin’ saved [3785248281/3785248281]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.chains import RetrievalQA\n",
        "from langchain.document_loaders import PyPDFLoader\n",
        "from langchain.embeddings import HuggingFaceEmbeddings\n",
        "from langchain.llms import GPT4All\n",
        "from langchain.text_splitter import RecursiveCharacterTextSplitter\n",
        "from langchain.vectorstores import Chroma\n",
        "from pdf2image import convert_from_path\n",
        "from langchain.retrievers.self_query.base import SelfQueryRetriever"
      ],
      "metadata": {
        "id": "gZHVgZIpUtaL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''from langchain.document_loaders import PyPDFDirectoryLoader\n",
        "loader = PyPDFDirectoryLoader('multiple docs')\n",
        "docs = loader.load()\n",
        "type(docs)\n",
        "print(docs)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rpwfNAHKHtXe",
        "outputId": "9f19167f-c5eb-449b-a3dc-88266721d789"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.document_loaders import PyPDFLoader\n",
        "loader = PyPDFLoader(\"/content/volkswagen.pdf\")\n",
        "docs = loader.load()"
      ],
      "metadata": {
        "id": "omuhMOPXsxRm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "documents = loader.load_and_split() #converted into documents for langchain"
      ],
      "metadata": {
        "id": "spayxuRJVQwm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "len(documents)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iWwCk0rxVU7G",
        "outputId": "a614dc7e-b78a-48e6-ae58-6031412050a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "49"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(documents[0].page_content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_F6NK16oVWYW",
        "outputId": "2303aa88-08c3-4114-d2d8-335da3e2f312"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Group Basic Software Requirements \n",
            "Basic requirements that the Volkswagen Group dem ands on vehicle-based and vehicle-related soft-\n",
            "ware.  \n",
            " \n",
            " \n",
            "Development, General Project-Indepen dent Performance Specification : LAH.893.909 \n",
            " \n",
            " \n",
            " \n",
            "First issue 06.09.2002 \n",
            "Date of revision 05.05.2023 \n",
            "Version 4.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64) #model has only 1000 tokens as limit , it will take both pages and convert it into text\n",
        "texts = text_splitter.split_documents(documents)"
      ],
      "metadata": {
        "id": "BnhnqFKqVX5K"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "len(texts)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8yWulKPTVan4",
        "outputId": "5100ea74-3cf5-46e4-9f86-013e8db1b2af"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "145"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(texts[0].page_content)\n",
        "#First page was divided into 2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sbOFkOOPVcHK",
        "outputId": "d129694c-630a-43ba-afc6-17da6b4b38d1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Group Basic Software Requirements \n",
            "Basic requirements that the Volkswagen Group dem ands on vehicle-based and vehicle-related soft-\n",
            "ware.  \n",
            " \n",
            " \n",
            "Development, General Project-Indepen dent Performance Specification : LAH.893.909 \n",
            " \n",
            " \n",
            " \n",
            "First issue 06.09.2002 \n",
            "Date of revision 05.05.2023 \n",
            "Version 4.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Create Embeddings to search for text\n",
        "embeddings = HuggingFaceEmbeddings(model_name=\"sentence-transformers/all-MiniLM-L6-v2\") #MiniLM created by microsoft\n"
      ],
      "metadata": {
        "id": "KZjfumVVVozQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        " #to store embeddings in vector database\n",
        "db = Chroma.from_documents(texts, embeddings, persist_directory=\"db\")\n",
        "#db.persists 3shan law 3yza t store it in your disk"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y9vT9tRqVua4",
        "outputId": "94aadaf6-fdf8-4b92-d1fb-e5c0d4b7b77e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb:Using embedded DuckDB with persistence: data will be stored in: db\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Create Chain\n",
        "#load gpt4all model\n",
        "model_n_ctx = 1000\n",
        "model_path = \"./ggml-gpt4all-j-v1.3-groovy.bin\"\n",
        "llm = GPT4All(model=model_path, n_ctx=1000, backend=\"gptj\",temp=0.9,verbose=False)\n",
        "#trauned with gpt-j"
      ],
      "metadata": {
        "id": "yTKy4eE3WO00"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Retrieval\n",
        "#we get source of document\n",
        "qa = RetrievalQA.from_chain_type(\n",
        "    llm=llm,\n",
        "    chain_type=\"stuff\",\n",
        "    retriever=db.as_retriever(search_kwargs={\"k\": 2}),\n",
        "    return_source_documents=True,\n",
        "    verbose=False,\n",
        ")"
      ],
      "metadata": {
        "id": "Qfp1RMVcWQXm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(res[\"result\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "elwlUoS6ZwTX",
        "outputId": "60839657-b633-4979-9218-5c76c3e4b2bc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " Generative AI use cases include many potential use cases across a business, including:\n",
            "\n",
            "* Generating sales copy, including marketing and sales material\n",
            "* Creating social media content or technical sales material, including presentations, demos, and training materials\n",
            "* Optimizing customer support chatbots\n",
            "* Developing custom customer support chatbots\n",
            "* Developing a custom support ticket system\n",
            "* Creating a customer support ticket system that integrates with existing tools\n",
            "* Developing a chatbot for customers who can't access customer support through phone or email\n",
            "* Developing a chatbot for customers who have multiple support inquiries at once\n",
            "* Developing a chatbot for customers who are experiencing issues with multiple products\n",
            "* Developing a chatbot for customers who are experiencing issues with multiple brands\n",
            "* Developing a chatbot for customers who are experiencing issues with multiple brands\n",
            "* Developing a chatbot for customers who are experiencing issues with multiple products\n",
            "* Developing a chatbot for customers who are experiencing issues with multiple brands\n",
            "* Developing a chatbot for customers who are experiencing issues with multiple brands\n",
            "* Developing a chatbot for customers who are experiencing issues with multiple brands\n",
            "* Developing a chatbot for customers who are experiencing issues with multiple brands\n",
            "* Developing\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%time\n",
        "prompt = f\"\"\"How much is the investment amount in Microsoft on 6/22? Extract the answer from the text.\"\"\"\n",
        "res = qa(prompt.strip())"
      ],
      "metadata": {
        "id": "8_3c2Tglc_lH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"Give examples of the main purposes of the KGAS.\"\n",
        ")"
      ],
      "metadata": {
        "id": "iehLD6uvdFHg",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ec55f579-2882-4e6a-d11d-b042f076c641"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 12min 37s, sys: 14.5 s, total: 12min 52s\n",
            "Wall time: 3min 37s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c-HYNBdwtogo",
        "outputId": "d729b526-0081-42bd-d5ca-5203c7fa97f2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'Give examples of the main purposes of the KGAS.',\n",
              " 'result': ' The main purpose of the KGAS is to provide a standardized framework for software development, testing, and maintenance. The KGAS includes guidelines, best practices, and tools for software development, testing, and maintenance. The KGAS is designed to be used by both developers and testers, and it is used to ensure that software is developed and tested according to established standards and best practices. The KGAS is also used to maintain software over time, by providing a framework for tracking changes and keeping software up to date.',\n",
              " 'source_documents': [Document(page_content='[R: KGAS_4000]  \\nThe contracting authority may have its analyses (KG AS_51) resulting from the KGAS performed in \\nfully or in partly carried out by third parties.', metadata={'source': '/content/volkswagen (1).pdf', 'page': 24}),\n",
              "  Document(page_content=\"[I: KGAS_2991]  \\nA component consists of units, encapsulates l ogically associated functionality and owns defined \\ninterfaces. \\n[I: KGAS_3641]  \\nComponents are represented in the softw are architecture specification. \\n[I: KGAS_3642]  \\nComponents are described in the software detailed design. \\n[I: KGAS_3102]  \\nA component, for example: contains one or more sour ce code files in C, one or more classes includ-\\ning inherited properties in object oriented programming languages (e.g. C++, Java). \\n4.7 Unit \\n[I: KGAS_2998]  \\nA unit is the smallest separately executable and testable entity of a component.  \\n[I: KGAS_2989]  \\nA unit encapsulates data and statements on the level of a function (C), method (C++, Java) or pro-\\ncedure (Pascal). \\n[I: KGAS_3643]  \\nUnits are described in the software detailed design. \\n4.8 Unit Element \\n[I: KGAS_3646]  \\nA unit's element is a part of a unit (e.g. calcul ations, interfaces, function calls or macros). \\n \\n[I: KGAS_3647]\", metadata={'source': '/content/volkswagen (1).pdf', 'page': 9})]}"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"Summarize the right of contracting authority.\"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rzYqjPwAunIF",
        "outputId": "26218b5b-cac8-4c5a-f613-a9e99f629848"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 10min 18s, sys: 2.55 s, total: 10min 21s\n",
            "Wall time: 2min 54s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kSnoNd8lvEHh",
        "outputId": "fe73f0fc-2400-40c4-853b-1a1c4bda48c4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'Summarize the right of contracting authority.',\n",
              " 'result': ' The contracting authority has the right to inspect the work performed by the contractor, and to require the contractor to provide an aggregate report of the work performed by a third party. The contracting authority may also require the contractor to nominate a third party to perform the work, and to ensure that the third party maintains confidentiality and complies with the requirements of the contract.',\n",
              " 'source_documents': [Document(page_content='[R: KGAS_4000]  \\nThe contracting authority may have its analyses (KG AS_51) resulting from the KGAS performed in \\nfully or in partly carried out by third parties.', metadata={'source': '/content/volkswagen (1).pdf', 'page': 24}),\n",
              "  Document(page_content=\"and software development processes and all corres ponding work products including the software \\nproduct. \\n[I: KGAS_3614]  \\nThe access (KGAS_2184) shall confirm to confidentiality  obligations of the contractor to third parties \\nin relation to requirements and content of such third parties. \\n[R: KGAS_1877]  \\nThe contracting authority may have its rights of inspection (KGAS_2184) arising from the KGAS \\nexercised in fully or in part by third parties. \\nThe contractor may request that an aggregated r eport be prepared by a third party to protect its \\nconfidential information. This report must ensure the evaluation of the quality of the contractor's \\nprocesses, but the information concerning the cont ractor's concrete proces s flow may be omitted. \\n[I: KGAS_2948]  \\nThe contracting authority shall nominate the third party to the contractor before commissioning of \\nthe third party (KGAS_1877). Third parties in this sense are obliged to maintain confidentiality and\", metadata={'source': '/content/volkswagen (1).pdf', 'page': 6})]}"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"List at least 5 items the training strategy must contain\"\n",
        ")"
      ],
      "metadata": {
        "id": "BklaGbUdzFit",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "60be0411-e2b4-4d79-a7af-188e11a66146"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 10min 47s, sys: 12.8 s, total: 11min\n",
            "Wall time: 3min 5s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fP7X9pTUE_8F",
        "outputId": "605f2c01-2998-4e38-c41c-da263543418c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'List at least 5 items the training strategy must contain',\n",
              " 'result': ' The training strategy must contain goals and procedures for the training of an architecture, including evaluation against so-called \"baseline models.\" The strategy must also contain a plan for modifying the training data and validation data according to the training strategy. There must also be evidence of the appropriate implementation of the data acquisition strategy, such as a review protocol. Additionally, there must be a plan for the choice of architecture, including evaluation against baseline models. The training strategy must also contain training end criteria.',\n",
              " 'source_documents': [Document(page_content='[A: KGAS_4083]  \\nThe training strategy must include goals and procedur e for training iterations including validation.', metadata={'source': '/content/volkswagen.pdf', 'page': 23}),\n",
              "  Document(page_content='[A: KGAS_4078]  \\nThe data acquisition strategy must include goals and procedure for modifying the training data and \\nvalidation data according to the training strategy. \\n[A: KGAS_4015]  \\nA data protection strategy must be defined and applied. The data protection strategy must fulfill the \\nGDPR and comparable applicable standards and laws.  \\n[A: KGAS_4011]  \\nEvidence of the appropriate implementation of th e data acquisition strategy must be documented \\nand made available to the contracting authority on reques t, e.g. in the form of a review protocol.  \\n5.7.4.3 Training und Testing \\n[A: KGAS_4012]  \\nThere must be a training strategy that contains input conditions.  \\n[A: KGAS_4081]  \\nThe training strategy must contain training end criteria.  \\n[A: KGAS_4082]  \\nThe training strategy must contain goals and proce dure for the choice of the architecture, including \\nthe evaluation against so-called \"baseline models\".  \\n[A: KGAS_4083]', metadata={'source': '/content/volkswagen.pdf', 'page': 23})]}"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"What is FOSS in 5 sentences \"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5eJ6gNkzHwV-",
        "outputId": "e8280283-c3d7-493b-efe4-8ff22db73b27"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 22min 35s, sys: 11.6 s, total: 22min 47s\n",
            "Wall time: 6min 22s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aFRQ47d1JCDr",
        "outputId": "3784b576-4321-432f-b3be-271a9b0941b0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'What is FOSS in 5 sentences ',\n",
              " 'result': ' FOFOS is a form of usage and licensing disclaimer for open source software. It is subject to sharing or disclosure of the source code of the software under substantial obligations. Contractor software is a third-party software that has been developed for the contractor or by themselves, but not against payment on behalf of the contracting authority. Contractor software is a third-party software that has been developed for the contractor or by themselves, but not against payment on behalf of the contracting authority. Contractor software is a third-party software that has been developed for the contractor or by themselves, but not against payment on behalf of the contracting authority. Contractor software is a third-party software that has been developed for the contractor or by themselves, but not against payment on behalf of the contracting authority. Contractor software is a third-party software that has been developed for the contractor or by themselves, but not against payment on behalf of the contracting authority. Contractor software is a third-party software that has been developed for the contractor or by themselves, but not against payment on behalf of the contracting authority. Contractor software is a third-party software that has been developed for the contractor or by themselves, but not against payment on behalf of the contracting authority. Contractor software is a third',\n",
              " 'source_documents': [Document(page_content=\"[I: KGAS_3924]  \\nThe contracting authority is responsib le for the technical condition of the auxiliary software as such. \\n5.14 Free and Open Source Software \\n[R: KGAS_3942]  \\nThis chapter applies to systems and software (del iverable) which uses Free and Open Source Soft-\\nware (see KGAS_3820). \\n[A: KGAS_3822]  \\nThe use of FOSS is only permitted if the contracting authority is informed in writing by the contractor \\nprior to the use of FOSS in accordance with the processes specified by th e contracting authority and \\nthe contractor confirms that the use of FOSS is in  accordance with the licence. The contractor com-\\nmits to operate the client's processes and, in parti cular, to observe possible written consent require-\\nments. \\n[I: KGAS_3821]  \\nA copyleft license is a form of usage and licensi ng disclaimers for open source software, which can \\nlead to the respective software elements integrat ed or linked with open source software being dis-\", metadata={'source': '/content/volkswagen.pdf', 'page': 33}),\n",
              "  Document(page_content='[I: KGAS_3919]  \\nThird-party software is a softw are which isn´t own software. \\n[I: KGAS_3921]  \\nAuxiliary software is a software whic h is provided by the contracting authority to the contractor within \\nthe fulfilment of the contract. This might be third-party or own software. \\n[I: KGAS_3820]  \\nFree and open source software (FOSS) is any softwar e that is distributed under the terms of use \\nand license terms for free and open source software and is subject to sharing or disclosure of the \\nsource code of the software under such substantial obligations. \\n[I: KGAS_3826]  \\nClosed source software is a software that is not  distributed under license terms for FOSS and whose \\nsource code is not freely accessible. \\n[I: KGAS_3952]  \\nContractor software is a third-party software that  has been developed for the contractor or by them-\\nself, but not against payment on behalf of the contracting authority. \\n[I: KGAS_3953]', metadata={'source': '/content/volkswagen.pdf', 'page': 10})]}"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"Describe in detail the quality assurance goals \"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MdquBUacQmyY",
        "outputId": "1b43953b-e032-4d65-bddc-97d2db958a40"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 22min 26s, sys: 25.1 s, total: 22min 51s\n",
            "Wall time: 6min 26s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zovDzVBZUJ0T",
        "outputId": "99b35e87-f6b9-4f0f-f868-e98272e9de87"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'Describe in detail the quality assurance goals ',\n",
              " 'result': '\\n\\nQuality assurance goals for a contractor should be based on a set of criteria that are measurable and specific to the product or service being produced. These goals should be set at a high enough level to ensure that the final product meets or exceeds customer expectations. The goals should be established through a thorough process that involves all relevant stakeholders, including the client, the contractor, and the relevant quality assurance department.\\n\\nThe goals should be evaluated regularly and adjusted as necessary to ensure that they are being met. This can be done through a combination of quantitative and qualitative data, as well as feedback from customers and stakeholders.\\n\\nIt is important for the contractor to be able to demonstrate their commitment to quality, and to do so through their own processes and systems. This can be done through a combination of training and education, as well as through ongoing quality assurance activities and feedback mechanisms.\\n\\nIn addition to the goals, the contractor should also have a clear and well-defined process for ensuring that all products produced are of high quality. This process should involve a thorough quality assurance system that is in place at all times, and that is regularly reviewed and updated as necessary.\\n\\nOverall, quality assurance goals should be based on a clear set of criteria that are measurable and specific to the product',\n",
              " 'source_documents': [Document(page_content=\"[A: KGAS_53]  \\nThe process and product quality assurance of the cont ractor must be personally and hierarchically \\nindependent from the product development. \\n[A: KGAS_2904]  \\nThe goals, evaluation methods, activities and criteria  of quality assurance of the contractor must not \\nbe influenced by the project lead. \\n[A: KGAS_3129]  \\nThe quality assurance goals must be measurable. \\n[A: KGAS_3130]  \\nA goal of quality assurance must be that all wo rk products mandated by the process are created and \\nquality assured in-time and in accordance with the process descriptions. \\n[A: KGAS_3133]  \\nOne goal of quality assurance must be that only qual ity-assured products are delivered to the con-\\ntracting authority.  \\n[A: KGAS_2911]  \\nThe quality assurance of the contractor must be involved in the release process of the software \\ndeliverables (at least by pr oviding a quality statement). \\n[A: KGAS_2913]  \\nEmployees of the contractor's quality assurance department must hav e the technical qualifications\", metadata={'source': '/content/volkswagen.pdf', 'page': 28}),\n",
              "  Document(page_content='[A: KGAS_2933]  \\nIf the contractor or its sub-contractors cannot fulfil the KGAS completely, the contractor must seek \\nwritten approval of the deviations from the Qualit y Assurance of the contracting authority before the \\nstart of the project. The agreed and approved c hanges are to be sent to Group Quality (contact \\nplease refer KGAS_2085). \\n[I: KGAS_2932]  \\nUnapproved deviations from the KGAS may result in  a downgrade of the quality capability rating of \\nthe contractor (also see KGAS_2834 \"Formula Q Capability Software\"). \\n[A: KGAS_3107]  \\nIf deviation from KGAS is identified, the contract or must promptly set up  an improvement program. \\n \\n[A: KGAS_42]  \\nThe improvement measures of th e improvement program (KGAS_31 07) must be carried out with \\ndefined scope and date, which must be agreed with the contracting authority. \\n[A: KGAS_2184]  \\nThe contractor must assure that the contracting authority is given the possibility to access the system', metadata={'source': '/content/volkswagen.pdf', 'page': 6})]}"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"List examples of Unit Test requirements in terms of coverage \"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ObVhh1rZWrA4",
        "outputId": "d359d3a6-87c5-42cf-87eb-4b1e21b5bc46"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 23min 4s, sys: 14 s, total: 23min 18s\n",
            "Wall time: 6min 33s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X0AKDnSKW7_K",
        "outputId": "522d322c-138f-4f6d-9a4b-e73a69facc10"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'List examples of Unit Test requirements in terms of coverage ',\n",
              " 'result': '\\n\\n* Example 1: A system has 10 functions, and the unit test is written to cover each function.\\n* Example 2: A software application has 10 modules, and the unit test is written to cover each module.\\n* Example 3: A hardware device has 10 sensors, and the unit test is written to cover each sensor.\\n* Example 4: A database has 10 tables, and the unit test is written to cover each table.\\n* Example 5: A software application has 10 pages, and the unit test is written to cover each page.\\n* Example 6: A software application has 10 features, and the unit test is written to cover each feature.\\n* Example 7: A hardware device has 10 settings, and the unit test is written to cover each setting.\\n* Example 8: A software application has 10 functions, and the unit test is written to cover each function.\\n* Example 9: A hardware device has 10 buttons, and the unit test is written to cover each button.\\n* Example 10: A software application has 10 modules, and the unit test is written to cover each module.\\n\\nThese examples show how unit tests can be written to cover specific areas of a system, application, or device. By covering these areas',\n",
              " 'source_documents': [Document(page_content='[A: KGAS_3335]  \\nThe test plan must include a description of how a complete test coverage of all specifications is \\nachieved (e.g. customer requirement  specification, interface specification, software requirement \\nspecification, software architecture s pecification, software detailed design). \\n[I: KGAS_3657]  \\nThe test plan (KGAS_3556) can contain a joint test  strategy of the contracting authority and contrac-\\ntor. \\n[A: KGAS_3336]  \\nThe test plan must define the test scopes separating t he test levels (e.g. system, system integration, \\nsoftware, software integration and unit test). \\n[A: KGAS_3338]  \\nThe test plan must include methods for test case creation, test case selection, creation of test data \\nand test execution. \\n[A: KGAS_3339]  \\nBlack-box test specifications must be created ba sed on requirements from respective architecture \\nspecifications and software detailed design. \\n[A: KGAS_3554]  \\nThe test plan must at least consider the following  software error types: divi sion by zero, overflows,', metadata={'source': '/content/volkswagen.pdf', 'page': 25}),\n",
              "  Document(page_content='The goal of each test case must be documented. \\n[A: KGAS_3358]  \\nThe expected nominal behavior of each test case must be documented. \\n[A: KGAS_3538]  \\nThe test steps must be documented for each test case. \\n[A: KGAS_3359]  \\nPossible boundary values must be tested for each requirement, interface, parameter, unit and deci-\\nsion point. \\n[A: KGAS_3362]  \\nPre and post conditions must be documented for each test case. \\n[A: KGAS_3363]  \\nIt must be possible to execute each test case independently. Mutual dependencies of test cases on \\neach other are not allowed. The setup of test chains to fulfill the test preconditions of lower-level test \\ncases is permitted, provided that this does not otherwise influence the test result. \\n[A: KGAS_3364]  \\nBlack-box tests must be specified before white-box tests. \\n[A: KGAS_3366]  \\nIf more than 10 test cases are necessary for verifica tion of a requirement, the quality of the require-', metadata={'source': '/content/volkswagen.pdf', 'page': 26})]}"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"What are the categories or types or requirements have to be assigned? \"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ADCTdYhmfxtU",
        "outputId": "e2e0ae89-db2d-429b-aa1b-8b8223d7b5df"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 11min 30s, sys: 2.43 s, total: 11min 32s\n",
            "Wall time: 3min 13s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fmCv05LTgOt3",
        "outputId": "ac9f250f-b87d-4b1c-f72d-b538914be3db"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'What are the categories or types or requirements have to be assigned? ',\n",
              " 'result': ' The categories or types or requirements have to be assigned are safety relevance, feasibility, verifiability, self-consistency, understandability, and traceability.',\n",
              " 'source_documents': [Document(page_content='[A: KGAS_3600]  \\nAll requirements must be evaluated regarding their impact on the system and software architecture. \\n \\n[A: KGAS_3558]  \\nAll requirements must be prioritized and categorized. \\n[A: KGAS_3257]  \\nAt least the following categorie s or types have to be assigned: \\n \\n\\uf0b7 safety relevance', metadata={'source': '/content/volkswagen.pdf', 'page': 15}),\n",
              "  Document(page_content='5.4 System and Software Re quirements Specification \\n[A: KGAS_3406]  \\nAll assumptions must be specified as requirem ents and agreed with the contracting authority. \\n \\n[A: KGAS_3548]  \\nOwn requirements of the contractor (e.g. require ments for production, requi rements from platform \\nparts, etc.) must be documented in the system  and software requirement specifications. \\n \\n[A: KGAS_3266]  \\nAll requirements must be verifiably created and anal yzed considering at leas t the following aspects: \\n \\n\\uf0b7 Feasibility \\n\\uf0b7 Verifiability \\n\\uf0b7 Self-consistency \\n\\uf0b7 Understandability \\n\\uf0b7 Unambiguousness \\n\\uf0b7 Atomicity \\n[A: KGAS_3535]  \\nAll requirements must be assigned to releases or features. \\n[A: KGAS_3259]  \\nAll requirements must be retr aceable to their sources. \\n[A: KGAS_3260]  \\nAll requirements must be traceable to the work products derived from them. \\n[A: KGAS_3256]  \\nFor all requirements the verification criteria in cluding a textual description must be documented. \\n \\n[A: KGAS_3600]', metadata={'source': '/content/volkswagen.pdf', 'page': 15})]}"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"What are the main components of project management?  \"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xppsQ0-9idN6",
        "outputId": "0e8f090c-63fa-4b7b-e093-1954ad512d48"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 9min 41s, sys: 2.32 s, total: 9min 44s\n",
            "Wall time: 2min 43s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fvwgre0CjMn2",
        "outputId": "13bec3a1-3808-42bc-eb79-73542f517067"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'What are the main components of project management?  ',\n",
              " 'result': ' The main components of project management are overall process requirements, project management, documentation of deliverables, system and software requirements, system and software architecture, software detail design, software construction, problem resolution management, and problem management system.',\n",
              " 'source_documents': [Document(page_content='5\\xa0 System and Software Development ............................................................................. 13 \\xa0\\n5.1\\xa0 Overall Process Requirements .................................................................................... 13 \\xa0\\n5.2\\xa0 Project Management .................................................................................................... 14 \\xa0\\n5.3\\xa0 Documentation of Deliverable ...................................................................................... 15 \\xa0\\n5.4\\xa0 System and Software Requirements Specification ...................................................... 16 \\xa0\\n5.5\\xa0 System and Software Architecture Specification ......................................................... 17 \\xa0\\n5.6\\xa0 Software Detailed Design............................................................................................. 18 \\xa0\\n5.7\\xa0 Software Construction .................................................................................................. 19', metadata={'source': '/content/volkswagen.pdf', 'page': 1}),\n",
              "  Document(page_content=\"5.11 Problem Resolution Management \\n[A: KGAS_3608]  \\nThe contractor must communicate all open for contra cting authority relevant product problems to the \\ncontracting authority at the time of delivery. \\n[A: KGAS_3410]  \\nThe contractor's problem management system mu st be able to properly map and document the \\ncontracting authoritys problem evaluation system in  order to exclude loss of information due to in-\\nsufficient interfaces. \\n[A: KGAS_3411]  \\nThe contractor's problem evaluation of all product pr oblems must be consistent with the contracting \\nauthoritys problem evaluation. \\n[A: KGAS_3412]  \\nProduct problems found in any test level must be processed by the problem management process.\", metadata={'source': '/content/volkswagen.pdf', 'page': 30})]}"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"How the usage of FOSS is permitted?  \"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oRagySSWj4Gu",
        "outputId": "a5370018-cc33-4cff-d308-33ba47f3d267"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 18min 17s, sys: 22.7 s, total: 18min 40s\n",
            "Wall time: 5min 15s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tOU_rCaKkyFP",
        "outputId": "7252c941-ff86-4f6f-83a7-2906e85b2b3f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'How the usage of FOSS is permitted?  ',\n",
              " 'result': '\\n\\nFOFSS (Free and Open Source Software) is a form of usage and licensing disclaimer for open source software. The contracting authority is responsible for the technical condition of the auxiliary software. The contractor is required to obtain written consent from the contracting authority before using FOFSS in accordance with the processes specified by the contracting authority and the contractor confirms that the use of FOFSS is in accordance with the license. The contractor must also confirm that no software element of the delivered software triggers a copylf effect, which leads to the software product as a whole being classified as FOFSS licensed under a copylf effect. The contractor may only use FOFSS in the delivered software which does not restrict the contractual and intended use of its services by the contracting authority and Volkswagen Group companies.',\n",
              " 'source_documents': [Document(page_content=\"[I: KGAS_3924]  \\nThe contracting authority is responsib le for the technical condition of the auxiliary software as such. \\n5.14 Free and Open Source Software \\n[R: KGAS_3942]  \\nThis chapter applies to systems and software (del iverable) which uses Free and Open Source Soft-\\nware (see KGAS_3820). \\n[A: KGAS_3822]  \\nThe use of FOSS is only permitted if the contracting authority is informed in writing by the contractor \\nprior to the use of FOSS in accordance with the processes specified by th e contracting authority and \\nthe contractor confirms that the use of FOSS is in  accordance with the licence. The contractor com-\\nmits to operate the client's processes and, in parti cular, to observe possible written consent require-\\nments. \\n[I: KGAS_3821]  \\nA copyleft license is a form of usage and licensi ng disclaimers for open source software, which can \\nlead to the respective software elements integrat ed or linked with open source software being dis-\", metadata={'source': '/content/volkswagen.pdf', 'page': 33}),\n",
              "  Document(page_content='tributed only under the respective usage and li cense terms of the copyleft license. \\n[I: KGAS_3840]  \\nA copyleft effect refers to the use of free and open source software under a copyleft license, and as \\na result of which any modification (\"each derivative work\") must also be classified as FOSS licensed \\nunder a copyleft license (see also KGAS_3821). \\n[A: KGAS_3833]  \\nThe contractor must confirm that no software el ement of the delivered software triggers a copyleft \\neffect, which leads to the software product as a whole being classified as FOSS licensed under a \\ncopyleft license. \\n[R: KGAS_3830]  \\nThe contractor may only use FOSS in  the delivered software which does not restrict the contractual \\nand intended use of its services by the c ontracting authority and Volkswagen Group companies. \\n \\n[A: KGAS_4097]  \\nAt the time of delivery of the software, the contra ctor grants the client the sub-licensable and trans-', metadata={'source': '/content/volkswagen.pdf', 'page': 33})]}"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"What is data acquisition strategy, and what does it include? \"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aY9IO4ConBGF",
        "outputId": "0a7b58e4-343e-4d54-bbad-acbe3f7a9305"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 15min 2s, sys: 17.2 s, total: 15min 19s\n",
            "Wall time: 4min 15s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CHCgAmjUn81u",
        "outputId": "d1978bfa-5db0-40c6-9557-5c961ca91ff3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'What is data acquisition strategy, and what does it include? ',\n",
              " 'result': ' The data acquisition strategy is a plan for acquiring, organizing, and using data in a specific application area. It includes goals and procedures for labeling, partitioning, archiving, and integrating data into configuration management. It also includes goals and procedures for modifying training and validation data according to the training strategy. The strategy must be documented and made available to the contracting authority on request.',\n",
              " 'source_documents': [Document(page_content='ments placed on the data. \\n[I: KGAS_4073]  \\nRepresentativeness is achieved when the generated, procured,  filtered and processed data repre-\\nsents the specified application area \\n[I: KGAS_4074]  \\nBalance is achieved when the generated, procured, fi ltered and processed data are distributed in \\naccordance with the requirements. \\n[A: KGAS_4075]  \\nThe data acquisition strategy must include goals and procedure for labeling the data; even in the \\ncase of unsupervised learning, a decision must be made about the need for individual labeled data \\nand, if necessary, an appropriate procedure defined. \\n[A: KGAS_4076]  \\nThe data acquisition strategy must include goals and proc edure for partitioning the data into training, \\ntesting, and validation data. \\n[A: KGAS_4077]  \\nThe data acquisition strategy must include goals and procedure for archiving the data (training, test, \\nand validation data) and for integrating it into configuration management. \\n[A: KGAS_4078]', metadata={'source': '/content/volkswagen.pdf', 'page': 23}),\n",
              "  Document(page_content='[A: KGAS_4078]  \\nThe data acquisition strategy must include goals and procedure for modifying the training data and \\nvalidation data according to the training strategy. \\n[A: KGAS_4015]  \\nA data protection strategy must be defined and applied. The data protection strategy must fulfill the \\nGDPR and comparable applicable standards and laws.  \\n[A: KGAS_4011]  \\nEvidence of the appropriate implementation of th e data acquisition strategy must be documented \\nand made available to the contracting authority on reques t, e.g. in the form of a review protocol.  \\n5.7.4.3 Training und Testing \\n[A: KGAS_4012]  \\nThere must be a training strategy that contains input conditions.  \\n[A: KGAS_4081]  \\nThe training strategy must contain training end criteria.  \\n[A: KGAS_4082]  \\nThe training strategy must contain goals and proce dure for the choice of the architecture, including \\nthe evaluation against so-called \"baseline models\".  \\n[A: KGAS_4083]', metadata={'source': '/content/volkswagen.pdf', 'page': 23})]}"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"How to select and use programming language of the software product? \"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_M9zaCD_pUjg",
        "outputId": "2a83f393-e30f-4c38-dea5-f3781d118a9e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 17min 37s, sys: 4.32 s, total: 17min 42s\n",
            "Wall time: 4min 59s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QlvocG5Wplyo",
        "outputId": "9f8be94e-8730-4cb6-c934-0a9fb48698f6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'How to select and use programming language of the software product? ',\n",
              " 'result': ' The programming language of the software product must be an international standardized (e.g. ISO/IEC) high-level programming language. The usage of different programming or script languages in the software product is only permitted after justification, verification of suitability, and approval by the contracting authority.\\n\\n5.7.2 Manual Code Construction ......................................................... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .',\n",
              " 'source_documents': [Document(page_content='ranges, error values and physical mapping. \\n[A: KGAS_3455]  \\nThe software detailed design must also be crea ted for every graphical or model-based program. \\n \\n[A: KGAS_3682]  \\nFor each interface a validation check against the interface description (KGAS_3276) must be spec-\\nified. \\n[A: KGAS_3683]  \\nIn the case of negative validity tests of inte rfaces, a defined system and software behavior must be \\nspecified. \\n5.7 Software Construction 5.7.1 Programming Languages \\n[A: KGAS_2050]  \\nThe programming language of the software product must be an international standardized (e.g. \\nISO/IEC) high-level programming language. \\n[A: KGAS_2837]  \\nThe usage of different programming or script languages in the software product is only permitted \\nafter justification, verification of suitability  and approval by the contracting authority. \\n5.7.2 Manual Code Construction \\n[R: KGAS_3948]  \\nThis chapter does just apply to software (deliv erable) which uses methods of manually encoded \\nprogramming. \\n[A: KGAS_3909]', metadata={'source': '/content/volkswagen.pdf', 'page': 18}),\n",
              "  Document(page_content='5.7.1\\xa0Programming Languages ............................................................................................. 19', metadata={'source': '/content/volkswagen.pdf', 'page': 1})]}"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"Describe in detail the quality assurance goals \"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WLxR6v4crNDM",
        "outputId": "6a056831-72bc-4586-a51e-bc681f6f4a2e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 18min 1s, sys: 17 s, total: 18min 18s\n",
            "Wall time: 5min 7s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FM0tTg01rYWA",
        "outputId": "44503c7a-3e7c-4c41-9778-08cc117af953"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'Describe in detail the quality assurance goals ',\n",
              " 'result': '\\n\\nQuality assurance goals for a software project involve ensuring that the project meets the specified requirements and objectives. These goals can be broken down into various areas, such as project design, product quality, testing, and release processes. The goals should be measurable and specific, and they should be regularly monitored and reviewed throughout the project. Quality assurance goals can also include implementing a quality management system, such as KGAS, and providing regular feedback to the contracting authority. The quality assurance goals are not influenced by the project lead, and they are independent from the product development process. The goals are not influenced by the project lead and are independent from the project.',\n",
              " 'source_documents': [Document(page_content=\"[A: KGAS_53]  \\nThe process and product quality assurance of the cont ractor must be personally and hierarchically \\nindependent from the product development. \\n[A: KGAS_2904]  \\nThe goals, evaluation methods, activities and criteria  of quality assurance of the contractor must not \\nbe influenced by the project lead. \\n[A: KGAS_3129]  \\nThe quality assurance goals must be measurable. \\n[A: KGAS_3130]  \\nA goal of quality assurance must be that all wo rk products mandated by the process are created and \\nquality assured in-time and in accordance with the process descriptions. \\n[A: KGAS_3133]  \\nOne goal of quality assurance must be that only qual ity-assured products are delivered to the con-\\ntracting authority.  \\n[A: KGAS_2911]  \\nThe quality assurance of the contractor must be involved in the release process of the software \\ndeliverables (at least by pr oviding a quality statement). \\n[A: KGAS_2913]  \\nEmployees of the contractor's quality assurance department must hav e the technical qualifications\", metadata={'source': '/content/volkswagen.pdf', 'page': 28}),\n",
              "  Document(page_content='[A: KGAS_2933]  \\nIf the contractor or its sub-contractors cannot fulfil the KGAS completely, the contractor must seek \\nwritten approval of the deviations from the Qualit y Assurance of the contracting authority before the \\nstart of the project. The agreed and approved c hanges are to be sent to Group Quality (contact \\nplease refer KGAS_2085). \\n[I: KGAS_2932]  \\nUnapproved deviations from the KGAS may result in  a downgrade of the quality capability rating of \\nthe contractor (also see KGAS_2834 \"Formula Q Capability Software\"). \\n[A: KGAS_3107]  \\nIf deviation from KGAS is identified, the contract or must promptly set up  an improvement program. \\n \\n[A: KGAS_42]  \\nThe improvement measures of th e improvement program (KGAS_31 07) must be carried out with \\ndefined scope and date, which must be agreed with the contracting authority. \\n[A: KGAS_2184]  \\nThe contractor must assure that the contracting authority is given the possibility to access the system', metadata={'source': '/content/volkswagen.pdf', 'page': 6})]}"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"What are the categories or types or requirements have to be assigned?\"\n",
        ")"
      ],
      "metadata": {
        "id": "GdNOT66GtM2u"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"Describe in details the General Cybersecurity Requirements\"\n",
        ")"
      ],
      "metadata": {
        "id": "uP6XHhvNt1vq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "59df8ece-f141-406b-b4d0-4ccba4b52123"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 19min 42s, sys: 21.4 s, total: 20min 4s\n",
            "Wall time: 5min 39s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CuV4nRalhFWQ",
        "outputId": "ad558326-297c-42b8-bfb6-f73ec609e693"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'Describe in details the General Cybersecurity Requirements',\n",
              " 'result': '\\n\\nThe General Cybersecurity Requirements document is a document that outlines the overall cybersecurity requirements for a system or software. It is a work product that documents the necessary cybersecurity requirements to successfully implement the system or software. The document is used to ensure that all cybersecurity requirements are met, and it is reviewed and updated as necessary to ensure that the system or software is secure. The document is typically reviewed by the appropriate department within the organization, such as the K-GQS department for the Volkswagen AG. The document is also reviewed by the appropriate government agencies, such as the Federal Office for Information Security (BSI) in Germany. The document is a critical component of the overall cybersecurity requirements for the system or software, and it is reviewed and updated as necessary to ensure that the system or software is secure.',\n",
              " 'source_documents': [Document(page_content='controls must be defined. \\n[A: KGAS_3750]  \\nCybersecurity controls must verifiably  lead to cybersecurity requirements. \\n[A: KGAS_3751]  \\nThe cybersecurity concept of the contractor must consider all risks. \\n5.15.5 Cybersecurity Riskmanagement \\n[A: KGAS_3745]  \\nIn case of changes at system and/or software level,  the cybersecurity risk analysis as well as the \\ncybersecurity concept must be updated accordingly. \\n[A: KGAS_3746]  \\nIn case of identification of new attack vector s against used technologies during development, all \\ncybersecurity risk analysis as well as the cy bersecurity concept must be updated accordingly. \\n \\n[A: KGAS_3980]  \\nIdentified weaknesses must be verifiably managed until  the risk has been minimized to an accepta-\\nble level. \\n[A: KGAS_3981]  \\nThe acceptance of residual risks must be justified. \\n5.15.6 Cybersecurity Architectural and Design \\n[A: KGAS_3753]  \\nSystem architecture, software architecture and de tailed design must verifiably cover all cybersecu-\\nrity requirements.', metadata={'source': '/content/volkswagen.pdf', 'page': 39}),\n",
              "  Document(page_content='Group Basic Software Requirements \\nGeneral Pro ject-Independent Performance Specification LAH.893.909   Page 38 of 48 \\n \\nPublic. All rights reserved. No part of this document may be provided to third parties or reproduced without the prior written consent of \\nthe appropriate Volkswagen AG department.  \\nThe English translation is believed to be accurate. In case of discrepancies, the German version controls. \\n© Volkswagen AG                                                   Department responsible for filing: K-GQS | CSD class: 4.5 – 15 years [I: KGAS_3712]  \\nCybersecurity Control \\nA cybersecurity control describes the (technical) r ealization of cybersecurity requirements to reduce \\nrisks and logically group cybersecurity requirements that are needed to successfully implement this \\ncybersecurity control. \\n[I: KGAS_3713]  \\nCybersecurity Concept \\nThe cybersecurity concept is a work product to doc ument cybersecurity relevant aspects of the de-', metadata={'source': '/content/volkswagen.pdf', 'page': 37})]}"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\n",
        "    \"Describe Briefly the General Cybersecurity Requirements\"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yjVpT5IfibeT",
        "outputId": "4af70241-feb8-41a0-965a-1b11c0d824d2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 15min 13s, sys: 13.2 s, total: 15min 27s\n",
            "Wall time: 4min 15s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KJpGTzb6jVAY",
        "outputId": "2ba4a18d-f87e-4888-998a-571d6d419e5a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'Describe Briefly the General Cybersecurity Requirements',\n",
              " 'result': ' The General Cybersecurity Requirements document outlines the overall cybersecurity requirements for a system or software. It includes a description of the system architecture, software architecture, and design, as well as the identification and management of identified weaknesses. The document also includes a description of the acceptance of residual risks and justification of the acceptance of residual risks. The document is filed by the appropriate Volkswagen AG department.',\n",
              " 'source_documents': [Document(page_content='controls must be defined. \\n[A: KGAS_3750]  \\nCybersecurity controls must verifiably  lead to cybersecurity requirements. \\n[A: KGAS_3751]  \\nThe cybersecurity concept of the contractor must consider all risks. \\n5.15.5 Cybersecurity Riskmanagement \\n[A: KGAS_3745]  \\nIn case of changes at system and/or software level,  the cybersecurity risk analysis as well as the \\ncybersecurity concept must be updated accordingly. \\n[A: KGAS_3746]  \\nIn case of identification of new attack vector s against used technologies during development, all \\ncybersecurity risk analysis as well as the cy bersecurity concept must be updated accordingly. \\n \\n[A: KGAS_3980]  \\nIdentified weaknesses must be verifiably managed until  the risk has been minimized to an accepta-\\nble level. \\n[A: KGAS_3981]  \\nThe acceptance of residual risks must be justified. \\n5.15.6 Cybersecurity Architectural and Design \\n[A: KGAS_3753]  \\nSystem architecture, software architecture and de tailed design must verifiably cover all cybersecu-\\nrity requirements.', metadata={'source': '/content/volkswagen.pdf', 'page': 39}),\n",
              "  Document(page_content='Group Basic Software Requirements \\nGeneral Pro ject-Independent Performance Specification LAH.893.909   Page 38 of 48 \\n \\nPublic. All rights reserved. No part of this document may be provided to third parties or reproduced without the prior written consent of \\nthe appropriate Volkswagen AG department.  \\nThe English translation is believed to be accurate. In case of discrepancies, the German version controls. \\n© Volkswagen AG                                                   Department responsible for filing: K-GQS | CSD class: 4.5 – 15 years [I: KGAS_3712]  \\nCybersecurity Control \\nA cybersecurity control describes the (technical) r ealization of cybersecurity requirements to reduce \\nrisks and logically group cybersecurity requirements that are needed to successfully implement this \\ncybersecurity control. \\n[I: KGAS_3713]  \\nCybersecurity Concept \\nThe cybersecurity concept is a work product to doc ument cybersecurity relevant aspects of the de-', metadata={'source': '/content/volkswagen.pdf', 'page': 37})]}"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Ask Questions\n",
        "%%time\n",
        "res = qa(\"Where is the documentation deliverable provided ?\"\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7W15YoOnk24Y",
        "outputId": "3aacdcd2-1e1d-43f9-dec4-18b2151c8974"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CPU times: user 17min 2s, sys: 4.26 s, total: 17min 7s\n",
            "Wall time: 4min 46s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res #0.1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CWsBqurOmyIS",
        "outputId": "245d63f3-b054-43f8-8f0f-4814da79be18"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'Where is the documentation deliverable provided ?',\n",
              " 'result': ' The documentation of deliverable is provided in Release No te s KGAS_4116, unless otherwise agreed between the contracting authority and the supplier. The documentation includes the release level (development stand without use on public road, development stand with use on public road, serial stand) of the delivery, the implemented changes in the scope of delivery, the tests carried out for the scope of the delivery, and the configuration status for the scope of delivery. The documentation also includes the release notes and the feature overviews of all scope s (modules) from sub-contractors.',\n",
              " 'source_documents': [Document(page_content='management and change management. \\n[A: KGAS_3178]  \\nExplicit definition for the degree of fulfillment of  work packages and activi ties must exist and be \\napplied. \\n[A: KGAS_3191]  \\nProject risks must be traceably identified,  evaluated and include counter measures. \\n5.3 Documentation of Deliverable \\n[A: KGAS_4115]  \\nThe documentation is provided in Release No tes KGAS_4116, unless otherwise agreed between \\nthe contracting authority and the supplier. \\n[A: KGAS_3214]  \\nThe release level (development stand without us e on public road, development stand with use on \\npublic road, serial stand) of the delivery must be documented. \\n[A: KGAS_3215]  \\nThe implemented changes in the scope of delivery must be documented, including a description of \\nany bug fixes. \\n[I: KGAS_3938]  \\nThe documentation also includes the release notes and the feature overviews of all scopes (e.g. \\nmodules) from sub-contractors. \\n[A: KGAS_3216]  \\nThe tests carried out for the scope of the delivery and their test results must be documented.', metadata={'source': '/content/volkswagen.pdf', 'page': 14}),\n",
              "  Document(page_content='[A: KGAS_3218]  \\nThe configuration status for the scope of delivery  (version of the software and possibly hardware, \\nmechanics etc.) must be documented (including vers ion, baseline, status of the underlying require-\\nments, the valid architecture, etc.). \\n[A: KGAS_3219]  \\nEach hardware version compatible with the softwar e version for the scope of the delivery must be \\ndocumented. \\n[A: KGAS_3220]  \\nEach software version compatible with the hardwar e version for the scope of the delivery must be \\ndocumented. \\n[A: KGAS_3221]  \\nAll constraints on the scope of delivery for co mmissioning and operation must be documented.', metadata={'source': '/content/volkswagen.pdf', 'page': 14})]}"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res #0.5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hn2LcfVMom-I",
        "outputId": "b32343e8-54e0-492e-d94a-0689f37d12f4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'Where is the documentation deliverable provided ?',\n",
              " 'result': ' The documentation of deliverable is provided in Release No. KGAS_4116, unless otherwise agreed between the contracting authority and the supplier. The documentation level is also documented in Release No. KGAS_3214. The implemented changes in the scope of delivery are documented in Release No. KGAS_3215. The tests carried out for the scope of delivery and their test results are documented in Release No. KGAS_393. The configuration status for the scope of delivery is documented in Release No. KGAS_3216. Each hardware version compatible with the software version for the scope of delivery is documented in Release No. KGAS_321. Each software version compatible with the hardware version for the scope of delivery is documented in Release No. KGAS_32. All constraints on the scope of delivery for configuration and operation are documented in Release No. KGAS_322.',\n",
              " 'source_documents': [Document(page_content='management and change management. \\n[A: KGAS_3178]  \\nExplicit definition for the degree of fulfillment of  work packages and activi ties must exist and be \\napplied. \\n[A: KGAS_3191]  \\nProject risks must be traceably identified,  evaluated and include counter measures. \\n5.3 Documentation of Deliverable \\n[A: KGAS_4115]  \\nThe documentation is provided in Release No tes KGAS_4116, unless otherwise agreed between \\nthe contracting authority and the supplier. \\n[A: KGAS_3214]  \\nThe release level (development stand without us e on public road, development stand with use on \\npublic road, serial stand) of the delivery must be documented. \\n[A: KGAS_3215]  \\nThe implemented changes in the scope of delivery must be documented, including a description of \\nany bug fixes. \\n[I: KGAS_3938]  \\nThe documentation also includes the release notes and the feature overviews of all scopes (e.g. \\nmodules) from sub-contractors. \\n[A: KGAS_3216]  \\nThe tests carried out for the scope of the delivery and their test results must be documented.', metadata={'source': '/content/volkswagen.pdf', 'page': 14}),\n",
              "  Document(page_content='[A: KGAS_3218]  \\nThe configuration status for the scope of delivery  (version of the software and possibly hardware, \\nmechanics etc.) must be documented (including vers ion, baseline, status of the underlying require-\\nments, the valid architecture, etc.). \\n[A: KGAS_3219]  \\nEach hardware version compatible with the softwar e version for the scope of the delivery must be \\ndocumented. \\n[A: KGAS_3220]  \\nEach software version compatible with the hardwar e version for the scope of the delivery must be \\ndocumented. \\n[A: KGAS_3221]  \\nAll constraints on the scope of delivery for co mmissioning and operation must be documented.', metadata={'source': '/content/volkswagen.pdf', 'page': 14})]}"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res #0.9"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MuRcc70xqh9b",
        "outputId": "6caaefa9-d85a-48f3-f3f7-ff5f1a50f5e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'query': 'Where is the documentation deliverable provided ?',\n",
              " 'result': ' The documentation of deliverable is provided in Release No. KGAS_4116, unless otherwise agreed between the contracting authority and the supplier. The documentation level is also documented in Release No. KGAS_321. The implemented changes in the scope of delivery are documented in Release No. KGAS_321. The tests carried out for the scope of delivery and their test results are documented in Release No. KGAS_393. The configuration status for the scope of delivery is documented in Release No. KGAS_321. Each hardware version compatible with the software version for the scope of delivery is documented in Release No. KGAS_321. Each software version compatible with the hardware version for the scope of delivery is documented in Release No. KGAS_32. All constraints on the scope of delivery for configuration and operation are documented in Release No. KGAS_322.',\n",
              " 'source_documents': [Document(page_content='management and change management. \\n[A: KGAS_3178]  \\nExplicit definition for the degree of fulfillment of  work packages and activi ties must exist and be \\napplied. \\n[A: KGAS_3191]  \\nProject risks must be traceably identified,  evaluated and include counter measures. \\n5.3 Documentation of Deliverable \\n[A: KGAS_4115]  \\nThe documentation is provided in Release No tes KGAS_4116, unless otherwise agreed between \\nthe contracting authority and the supplier. \\n[A: KGAS_3214]  \\nThe release level (development stand without us e on public road, development stand with use on \\npublic road, serial stand) of the delivery must be documented. \\n[A: KGAS_3215]  \\nThe implemented changes in the scope of delivery must be documented, including a description of \\nany bug fixes. \\n[I: KGAS_3938]  \\nThe documentation also includes the release notes and the feature overviews of all scopes (e.g. \\nmodules) from sub-contractors. \\n[A: KGAS_3216]  \\nThe tests carried out for the scope of the delivery and their test results must be documented.', metadata={'source': '/content/volkswagen.pdf', 'page': 14}),\n",
              "  Document(page_content='[A: KGAS_3218]  \\nThe configuration status for the scope of delivery  (version of the software and possibly hardware, \\nmechanics etc.) must be documented (including vers ion, baseline, status of the underlying require-\\nments, the valid architecture, etc.). \\n[A: KGAS_3219]  \\nEach hardware version compatible with the softwar e version for the scope of the delivery must be \\ndocumented. \\n[A: KGAS_3220]  \\nEach software version compatible with the hardwar e version for the scope of the delivery must be \\ndocumented. \\n[A: KGAS_3221]  \\nAll constraints on the scope of delivery for co mmissioning and operation must be documented.', metadata={'source': '/content/volkswagen.pdf', 'page': 14})]}"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Vbq6rWgYt8P6"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}