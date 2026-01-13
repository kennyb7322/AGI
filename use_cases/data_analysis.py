"""
AGI Framework - Data Analysis Use Case
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Complete use case: AI-powered data analysis and insights
"""

import sys
import os
from datetime import datetime
import json

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agi import AGIModel, InferenceEngine
from agi.utils import PromptEngineer


class DataAnalysisAGI:
    """AI-powered data analysis system."""
    
    def __init__(self):
        """Initialize data analysis AGI."""
        self.model = AGIModel(
            model_name="AGI-DataAnalyst",
            version="1.0.0",
            config={"temperature": 0.5, "max_length": 1024}
        )
        
        self.inference_engine = InferenceEngine(self.model)
        self.prompt_engineer = PromptEngineer()
        
        # Setup analysis templates
        self._setup_templates()
        
        # Train the model
        self._train_model()
    
    def _setup_templates(self):
        """Setup data analysis templates."""
        self.prompt_engineer.create_template(
            "data_summary",
            """Analyze the following dataset and provide a comprehensive summary:

Dataset: {dataset_name}
Data: {data}

Provide:
1. Overview of the data
2. Key statistics
3. Notable patterns or trends
4. Potential insights

Analysis:"""
        )
        
        self.prompt_engineer.create_template(
            "trend_analysis",
            """Perform trend analysis on the following time series data:

Metric: {metric}
Time Period: {time_period}
Data Points: {data_points}

Identify:
1. Overall trend (increasing/decreasing/stable)
2. Seasonal patterns
3. Anomalies or outliers
4. Predictions for next period

Analysis:"""
        )
        
        self.prompt_engineer.create_template(
            "comparison_analysis",
            """Compare the following datasets:

Dataset A: {dataset_a}
Dataset B: {dataset_b}

Context: {context}

Provide:
1. Similarities
2. Differences
3. Relative performance
4. Recommendations

Comparison:"""
        )
    
    def _train_model(self):
        """Train the data analysis model."""
        training_data = [
            "The data shows an upward trend with seasonal variations...",
            "Analysis reveals strong correlation between variables...",
            "Key insights include performance improvements and growth...",
        ] * 15
        
        self.model.train(training_data, epochs=5)
    
    def summarize_data(self, dataset_name: str, data: dict) -> dict:
        """Generate data summary and insights."""
        template = self.prompt_engineer.get_template("data_summary")
        prompt = template.format(
            dataset_name=dataset_name,
            data=json.dumps(data, indent=2)
        )
        
        analysis = self.inference_engine.generate(prompt, temperature=0.4)
        
        return {
            "type": "data_summary",
            "dataset_name": dataset_name,
            "analysis": analysis,
            "timestamp": datetime.now().isoformat()
        }
    
    def analyze_trends(
        self,
        metric: str,
        time_period: str,
        data_points: list
    ) -> dict:
        """Analyze trends in time series data."""
        template = self.prompt_engineer.get_template("trend_analysis")
        prompt = template.format(
            metric=metric,
            time_period=time_period,
            data_points=json.dumps(data_points)
        )
        
        analysis = self.inference_engine.generate(prompt, temperature=0.4)
        
        return {
            "type": "trend_analysis",
            "metric": metric,
            "analysis": analysis,
            "timestamp": datetime.now().isoformat()
        }
    
    def compare_datasets(
        self,
        dataset_a: dict,
        dataset_b: dict,
        context: str
    ) -> dict:
        """Compare two datasets."""
        template = self.prompt_engineer.get_template("comparison_analysis")
        prompt = template.format(
            dataset_a=json.dumps(dataset_a),
            dataset_b=json.dumps(dataset_b),
            context=context
        )
        
        analysis = self.inference_engine.generate(prompt, temperature=0.45)
        
        return {
            "type": "comparison",
            "analysis": analysis,
            "timestamp": datetime.now().isoformat()
        }
    
    def generate_insights(self, data_description: str) -> dict:
        """Generate actionable insights from data description."""
        instruction = self.prompt_engineer.create_instruction_prompt(
            instruction="Generate actionable business insights from the data",
            context=data_description,
            constraints=[
                "Focus on actionable recommendations",
                "Prioritize insights by impact",
                "Include specific metrics where possible"
            ]
        )
        
        insights = self.inference_engine.generate(instruction, temperature=0.5)
        
        return {
            "type": "insights",
            "insights": insights,
            "timestamp": datetime.now().isoformat()
        }
    
    def explain_data_pattern(self, pattern_description: str) -> dict:
        """Explain observed data patterns."""
        cot_prompt = self.prompt_engineer.create_chain_of_thought_prompt(
            f"Explain the following data pattern: {pattern_description}",
            include_reasoning=True
        )
        
        explanation = self.inference_engine.generate(cot_prompt, temperature=0.4)
        
        return {
            "type": "pattern_explanation",
            "explanation": explanation,
            "timestamp": datetime.now().isoformat()
        }


def main():
    """Main data analysis use case demonstration."""
    print("=" * 60)
    print("AGI Framework - Data Analysis Use Case")
    print("Copyright (c) 2026 kennyb7322")
    print("=" * 60)
    print()
    
    # Initialize data analyst
    print("Initializing Data Analysis AGI...")
    analyst = DataAnalysisAGI()
    print("Data Analyst ready!")
    print()
    
    # Example 1: Data Summary
    print("=" * 60)
    print("Example 1: Dataset Summary and Insights")
    print("=" * 60)
    print()
    
    sales_data = {
        "total_revenue": 1250000,
        "total_orders": 5420,
        "average_order_value": 230.61,
        "top_products": ["Product A", "Product B", "Product C"],
        "customer_satisfaction": 4.5,
        "return_rate": 2.3
    }
    
    summary = analyst.summarize_data("Q1 Sales Data", sales_data)
    print(f"Dataset: {summary['dataset_name']}")
    print(f"Analysis:\n{summary['analysis']}")
    print()
    
    # Example 2: Trend Analysis
    print("=" * 60)
    print("Example 2: Trend Analysis")
    print("=" * 60)
    print()
    
    monthly_revenue = [
        {"month": "Jan", "revenue": 400000},
        {"month": "Feb", "revenue": 425000},
        {"month": "Mar", "revenue": 425000},
        {"month": "Apr", "revenue": 450000},
        {"month": "May", "revenue": 475000},
        {"month": "Jun", "revenue": 500000},
    ]
    
    trends = analyst.analyze_trends(
        metric="Monthly Revenue",
        time_period="January - June 2026",
        data_points=monthly_revenue
    )
    
    print(f"Metric: {trends['metric']}")
    print(f"Trend Analysis:\n{trends['analysis']}")
    print()
    
    # Example 3: Dataset Comparison
    print("=" * 60)
    print("Example 3: Dataset Comparison")
    print("=" * 60)
    print()
    
    dataset_2025 = {
        "revenue": 4800000,
        "customers": 12500,
        "avg_order": 220
    }
    
    dataset_2026 = {
        "revenue": 6200000,
        "customers": 15800,
        "avg_order": 235
    }
    
    comparison = analyst.compare_datasets(
        dataset_2025,
        dataset_2026,
        "Year-over-year business performance comparison"
    )
    
    print("Comparison Analysis:")
    print(comparison['analysis'])
    print()
    
    # Example 4: Generate Insights
    print("=" * 60)
    print("Example 4: Actionable Insights Generation")
    print("=" * 60)
    print()
    
    data_description = """
    E-commerce platform data shows:
    - 35% increase in mobile traffic
    - 15% decrease in desktop conversions
    - Cart abandonment rate at 68%
    - Customer acquisition cost increased by 20%
    - Repeat purchase rate at 40%
    """
    
    insights = analyst.generate_insights(data_description)
    print("Generated Insights:")
    print(insights['insights'])
    print()
    
    # Example 5: Pattern Explanation
    print("=" * 60)
    print("Example 5: Data Pattern Explanation")
    print("=" * 60)
    print()
    
    pattern = """
    Sales spike every Friday evening and Sunday afternoon, 
    with a significant drop on Tuesday mornings. 
    This pattern has been consistent for the past 3 months.
    """
    
    explanation = analyst.explain_data_pattern(pattern)
    print("Pattern Explanation:")
    print(explanation['explanation'])
    print()
    
    # Example 6: Multiple Analysis Tasks
    print("=" * 60)
    print("Example 6: Batch Analysis")
    print("=" * 60)
    print()
    
    metrics_to_analyze = [
        {"name": "User Engagement", "value": "Up 25% month-over-month"},
        {"name": "Churn Rate", "value": "Decreased from 5% to 3.5%"},
        {"name": "Feature Adoption", "value": "New feature used by 60% of users"}
    ]
    
    print("Analyzing multiple metrics...")
    for metric in metrics_to_analyze:
        print(f"  • {metric['name']}: {metric['value']}")
    print()
    
    # Display statistics
    print("=" * 60)
    print("Analysis Statistics")
    print("=" * 60)
    stats = analyst.inference_engine.get_statistics()
    print(f"Total analyses performed: {stats['total_requests']}")
    print(f"Total tokens generated: {stats['total_tokens_generated']}")
    print(f"Average analysis time: {stats['average_latency']:.4f}s")
    print()
    
    print("=" * 60)
    print("Data Analysis Use Case Complete!")
    print("=" * 60)
    print()
    print("Key Features Demonstrated:")
    print("  ✓ Dataset summarization")
    print("  ✓ Trend analysis")
    print("  ✓ Comparative analysis")
    print("  ✓ Insight generation")
    print("  ✓ Pattern explanation")
    print("  ✓ Chain-of-thought reasoning")


if __name__ == "__main__":
    main()
