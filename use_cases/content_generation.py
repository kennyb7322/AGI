"""
AGI Framework - Content Generation Use Case
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Complete use case: Automated content generation system
"""

import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agi import AGIModel, InferenceEngine, ModelTrainer
from agi.core import TrainingConfig
from agi.utils import PromptEngineer


class ContentGenerator:
    """Automated content generation system."""
    
    def __init__(self):
        """Initialize content generator."""
        self.model = AGIModel(
            model_name="AGI-ContentGenerator",
            version="1.0.0",
            config={"temperature": 0.8, "max_length": 1024}
        )
        
        self.inference_engine = InferenceEngine(self.model)
        self.prompt_engineer = PromptEngineer()
        
        # Setup content templates
        self._setup_templates()
        
        # Train the model
        self._train_model()
    
    def _setup_templates(self):
        """Setup content generation templates."""
        # Blog post template
        self.prompt_engineer.create_template(
            "blog_post",
            """Write a blog post about {topic}.

Title: {title}
Target Audience: {audience}
Tone: {tone}
Word Count: ~{word_count} words

Structure:
1. Engaging introduction
2. Main content with key points
3. Conclusion with call-to-action

Blog Post:"""
        )
        
        # Social media template
        self.prompt_engineer.create_template(
            "social_media",
            """Create a {platform} post about {topic}.
Tone: {tone}
Include: {include_elements}

Post:"""
        )
        
        # Product description template
        self.prompt_engineer.create_template(
            "product_description",
            """Write a compelling product description for:

Product Name: {product_name}
Category: {category}
Key Features: {features}
Target Customer: {target_customer}

Description:"""
        )
        
        # Email template
        self.prompt_engineer.create_template(
            "email",
            """Write a {email_type} email.

Subject: {subject}
Recipient: {recipient}
Purpose: {purpose}
Tone: {tone}

Email:"""
        )
    
    def _train_model(self):
        """Train the content generation model."""
        training_data = [
            "This is a sample blog post about technology...",
            "Product features include high quality and durability...",
            "Dear valued customer, we are pleased to announce...",
        ] * 15
        
        config = TrainingConfig(epochs=5, batch_size=16)
        trainer = ModelTrainer(self.model, config)
        trainer.train(training_data)
    
    def generate_blog_post(
        self,
        topic: str,
        title: str,
        audience: str = "general readers",
        tone: str = "informative and engaging",
        word_count: int = 500
    ) -> dict:
        """Generate a blog post."""
        template = self.prompt_engineer.get_template("blog_post")
        prompt = template.format(
            topic=topic,
            title=title,
            audience=audience,
            tone=tone,
            word_count=word_count
        )
        
        content = self.inference_engine.generate(prompt, temperature=0.8)
        
        return {
            "type": "blog_post",
            "title": title,
            "topic": topic,
            "content": content,
            "metadata": {
                "audience": audience,
                "tone": tone,
                "generated_at": datetime.now().isoformat()
            }
        }
    
    def generate_social_media_post(
        self,
        platform: str,
        topic: str,
        tone: str = "casual",
        include_elements: str = "hashtags and call-to-action"
    ) -> dict:
        """Generate a social media post."""
        template = self.prompt_engineer.get_template("social_media")
        prompt = template.format(
            platform=platform,
            topic=topic,
            tone=tone,
            include_elements=include_elements
        )
        
        content = self.inference_engine.generate(prompt, temperature=0.85)
        
        return {
            "type": "social_media",
            "platform": platform,
            "topic": topic,
            "content": content,
            "generated_at": datetime.now().isoformat()
        }
    
    def generate_product_description(
        self,
        product_name: str,
        category: str,
        features: str,
        target_customer: str
    ) -> dict:
        """Generate product description."""
        template = self.prompt_engineer.get_template("product_description")
        prompt = template.format(
            product_name=product_name,
            category=category,
            features=features,
            target_customer=target_customer
        )
        
        content = self.inference_engine.generate(prompt, temperature=0.75)
        
        return {
            "type": "product_description",
            "product_name": product_name,
            "content": content,
            "generated_at": datetime.now().isoformat()
        }
    
    def generate_email(
        self,
        email_type: str,
        subject: str,
        recipient: str,
        purpose: str,
        tone: str = "professional"
    ) -> dict:
        """Generate email content."""
        template = self.prompt_engineer.get_template("email")
        prompt = template.format(
            email_type=email_type,
            subject=subject,
            recipient=recipient,
            purpose=purpose,
            tone=tone
        )
        
        content = self.inference_engine.generate(prompt, temperature=0.7)
        
        return {
            "type": "email",
            "email_type": email_type,
            "subject": subject,
            "content": content,
            "generated_at": datetime.now().isoformat()
        }
    
    def batch_generate(self, content_requests: list) -> list:
        """Generate multiple content pieces in batch."""
        return self.inference_engine.batch_generate(
            [req["prompt"] for req in content_requests]
        )


def main():
    """Main content generation use case demonstration."""
    print("=" * 60)
    print("AGI Framework - Content Generation Use Case")
    print("Copyright (c) 2026 kennyb7322")
    print("=" * 60)
    print()
    
    # Initialize content generator
    print("Initializing Content Generator...")
    generator = ContentGenerator()
    print("Content Generator ready!")
    print()
    
    # Example 1: Generate Blog Post
    print("=" * 60)
    print("Example 1: Blog Post Generation")
    print("=" * 60)
    print()
    
    blog = generator.generate_blog_post(
        topic="Artificial Intelligence in Healthcare",
        title="How AI is Transforming Healthcare in 2026",
        audience="healthcare professionals and tech enthusiasts",
        tone="informative yet accessible",
        word_count=600
    )
    
    print(f"Blog Post Title: {blog['title']}")
    print(f"Topic: {blog['topic']}")
    print(f"Generated Content:\n{blog['content']}")
    print()
    
    # Example 2: Generate Social Media Posts
    print("=" * 60)
    print("Example 2: Social Media Post Generation")
    print("=" * 60)
    print()
    
    platforms = ["Twitter", "LinkedIn", "Instagram"]
    
    for platform in platforms:
        post = generator.generate_social_media_post(
            platform=platform,
            topic="AGI Framework Launch",
            tone="exciting and professional"
        )
        
        print(f"{platform} Post:")
        print(f"{post['content']}")
        print()
    
    # Example 3: Generate Product Descriptions
    print("=" * 60)
    print("Example 3: Product Description Generation")
    print("=" * 60)
    print()
    
    products = [
        {
            "product_name": "SmartWatch Pro",
            "category": "Wearable Technology",
            "features": "Heart rate monitoring, GPS, waterproof, 7-day battery",
            "target_customer": "fitness enthusiasts and busy professionals"
        },
        {
            "product_name": "EcoBottle",
            "category": "Sustainable Products",
            "features": "100% recycled materials, temperature control, leak-proof",
            "target_customer": "environmentally conscious consumers"
        }
    ]
    
    for product_spec in products:
        description = generator.generate_product_description(**product_spec)
        
        print(f"Product: {description['product_name']}")
        print(f"Description:\n{description['content']}")
        print()
    
    # Example 4: Generate Emails
    print("=" * 60)
    print("Example 4: Email Generation")
    print("=" * 60)
    print()
    
    emails = [
        {
            "email_type": "welcome",
            "subject": "Welcome to AGI Framework!",
            "recipient": "New User",
            "purpose": "Welcome new users and guide them through getting started",
            "tone": "warm and helpful"
        },
        {
            "email_type": "newsletter",
            "subject": "Monthly AGI Framework Updates",
            "recipient": "Subscribers",
            "purpose": "Share latest features and community highlights",
            "tone": "informative and engaging"
        }
    ]
    
    for email_spec in emails:
        email = generator.generate_email(**email_spec)
        
        print(f"Email Type: {email['email_type']}")
        print(f"Subject: {email['subject']}")
        print(f"Content:\n{email['content']}")
        print()
    
    # Display statistics
    print("=" * 60)
    print("Content Generation Statistics")
    print("=" * 60)
    stats = generator.inference_engine.get_statistics()
    print(f"Total content pieces generated: {stats['total_requests']}")
    print(f"Total tokens generated: {stats['total_tokens_generated']}")
    print(f"Average generation time: {stats['average_latency']:.4f}s")
    print()
    
    print("=" * 60)
    print("Content Generation Use Case Complete!")
    print("=" * 60)
    print()
    print("Key Features Demonstrated:")
    print("  ✓ Blog post generation")
    print("  ✓ Social media content creation")
    print("  ✓ Product description writing")
    print("  ✓ Email content generation")
    print("  ✓ Template-based generation")
    print("  ✓ Batch processing capability")


if __name__ == "__main__":
    main()
