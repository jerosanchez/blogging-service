-- Sample data
INSERT INTO
    posts (
        id,
        title,
        content,
        published,
        rating,
        created_at
    )
VALUES
    -- John Doe's posts (3)
    (
        'e2f1c3b4-5d6e-7a8b-9c0d-1e2f3a4b5c6d',
        'Getting Started with FastAPI for AI Projects',
        'FastAPI is a modern Python web framework that makes it easy to build APIs for machine learning models. In this post, I share tips for structuring your first AI backend.',
        true,
        5,
        '2025-12-03T14:22:00Z'
    ),
    (
        'f4e3d2c1-b5a6-7c8d-9e0f-1a2b3c4d5e6f',
        'Deploying Machine Learning Models with Docker',
        'Containerization simplifies the deployment of AI models. Here, I explain how to use Docker to package and serve your machine learning models efficiently.',
        false,
        3,
        '2025-12-07T10:45:00Z'
    ),
    (
        'a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d',
        'Best Practices for Training Neural Networks',
        'Training deep learning models can be tricky. This article covers essential practices like data normalization, regularization, and monitoring validation loss.',
        true,
        4,
        '2025-12-10T18:33:00Z'
    ),

-- Alice Smith's posts (5)
(
    'b7c8d9e0-1f2a-3b4c-5d6e-7f8a9b0c1d2e',
    'Building Chatbots with NLP',
    'Natural Language Processing enables the creation of intelligent chatbots. This post explores libraries and techniques for building conversational AI.',
    true,
    5,
    '2025-12-12T09:12:00Z'
),
(
    'c8d9e0f1-2a3b-4c5d-6e7f-8a9b0c1d2e3f',
    'Fine-Tuning Transformers for Custom Tasks',
    'Transformers have revolutionized NLP. Learn how to fine-tune pre-trained models for your own datasets and tasks.',
    true,
    4,
    '2025-12-15T21:05:00Z'
),
(
    'd9e0f1a2-3b4c-5d6e-7f8a-9b0c1d2e3f4a',
    'Serving AI Models with FastAPI and Uvicorn',
    'FastAPI and Uvicorn make it easy to serve AI models in production. This post covers deployment strategies and performance tips.',
    true,
    5,
    '2025-12-18T16:50:00Z'
),
(
    'e0f1a2b3-4c5d-6e7f-8a9b-0c1d2e3f4a5b',
    'Monitoring AI Model Performance in Production',
    'Monitoring deployed models is crucial for reliability. Here are tools and metrics to track your AI systems in real time.',
    false,
    3,
    '2025-12-21T11:27:00Z'
),
(
    'f1a2b3c4-5d6e-7f8a-9b0c-1d2e3f4a5b6c',
    'Automating Data Labeling for Machine Learning',
    'Efficient data labeling accelerates AI development. This article discusses automation tools and best practices for labeling datasets.',
    true,
    4,
    '2025-12-23T08:41:00Z'
),

-- Bob Jones's posts (4)
(
    'a2b3c4d5-e6f7-8a9b-0c1d-2e3f4a5b6c7d',
    'Introduction to Computer Vision with PyTorch',
    'PyTorch is a flexible framework for computer vision tasks. This post introduces image classification and transfer learning with PyTorch.',
    true,
    5,
    '2025-12-05T13:00:00Z'
),
(
    'b3c4d5e6-f7a8-9b0c-1d2e-3f4a5b6c7d8e',
    'Optimizing Inference Speed for AI APIs',
    'Speed is critical for AI-powered APIs. Learn how to optimize inference time using batching, quantization, and hardware acceleration.',
    true,
    4,
    '2025-12-09T09:45:00Z'
),
(
    'c4d5e6f7-a8b9-0c1d-2e3f-4a5b6c7d8e9f',
    'Data Augmentation Techniques for Deep Learning',
    'Data augmentation can improve model generalization. This post reviews popular augmentation methods for images and text.',
    false,
    3,
    '2025-12-14T17:25:00Z'
),
(
    'd5e6f7a8-b9c0-1d2e-3f4a-5b6c7d8e9f0b',
    'Using GPUs for Scalable AI Training',
    'GPUs accelerate deep learning training. Here, I discuss how to leverage GPU resources for faster model development and experimentation.',
    true,
    5,
    '2025-12-28T21:10:00Z'
)