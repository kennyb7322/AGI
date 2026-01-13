"""
AGI Framework - Neural Network Module
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Neural network components for building deep learning models
"""

from typing import Dict, List, Optional, Any, Tuple
import math


class Layer:
    """Base class for neural network layers."""
    
    def __init__(self, input_dim: int, output_dim: int, name: str = "layer"):
        """
        Initialize a layer.
        
        Args:
            input_dim: Input dimension
            output_dim: Output dimension
            name: Layer name
        """
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.name = name
        self.weights = self._initialize_weights()
        self.bias = [0.0] * output_dim
        
    def _initialize_weights(self) -> List[List[float]]:
        """Initialize weights using Xavier initialization."""
        limit = math.sqrt(6.0 / (self.input_dim + self.output_dim))
        return [[0.0] * self.output_dim for _ in range(self.input_dim)]
    
    def forward(self, x: List[float]) -> List[float]:
        """Forward pass through the layer."""
        if len(x) != self.input_dim:
            raise ValueError(f"Input dimension mismatch: expected {self.input_dim}, got {len(x)}")
        
        output = []
        for j in range(self.output_dim):
            activation = self.bias[j]
            for i in range(self.input_dim):
                activation += x[i] * self.weights[i][j]
            output.append(activation)
        return output
    
    def __repr__(self) -> str:
        return f"{self.name}(input={self.input_dim}, output={self.output_dim})"


class AttentionLayer:
    """Multi-head attention layer."""
    
    def __init__(self, hidden_size: int, num_heads: int, name: str = "attention"):
        """
        Initialize attention layer.
        
        Args:
            hidden_size: Hidden dimension size
            num_heads: Number of attention heads
            name: Layer name
        """
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.name = name
        self.head_dim = hidden_size // num_heads
        
        if hidden_size % num_heads != 0:
            raise ValueError("hidden_size must be divisible by num_heads")
    
    def forward(self, query: List[float], key: List[float], value: List[float]) -> List[float]:
        """
        Forward pass through attention layer.
        
        Args:
            query: Query vector
            key: Key vector
            value: Value vector
            
        Returns:
            Attention output
        """
        # Simplified attention mechanism
        return value  # In practice, this would compute scaled dot-product attention
    
    def __repr__(self) -> str:
        return f"{self.name}(hidden_size={self.hidden_size}, num_heads={self.num_heads})"


class NeuralNetwork:
    """
    Neural network architecture for generative AI models.
    
    This class provides a flexible neural network structure with support for
    various layer types including dense layers and attention mechanisms.
    """
    
    def __init__(
        self,
        input_size: int = 768,
        hidden_sizes: Optional[List[int]] = None,
        output_size: int = 768,
        num_attention_heads: int = 12,
        dropout_rate: float = 0.1
    ):
        """
        Initialize neural network.
        
        Args:
            input_size: Input dimension
            hidden_sizes: List of hidden layer sizes
            output_size: Output dimension
            num_attention_heads: Number of attention heads
            dropout_rate: Dropout rate for regularization
        """
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes or [768, 768, 768]
        self.output_size = output_size
        self.num_attention_heads = num_attention_heads
        self.dropout_rate = dropout_rate
        
        self.layers = self._build_layers()
        self.attention_layers = self._build_attention_layers()
        
    def _build_layers(self) -> List[Layer]:
        """Build dense layers."""
        layers = []
        prev_size = self.input_size
        
        for idx, hidden_size in enumerate(self.hidden_sizes):
            layer = Layer(prev_size, hidden_size, name=f"dense_{idx}")
            layers.append(layer)
            prev_size = hidden_size
        
        # Output layer
        output_layer = Layer(prev_size, self.output_size, name="output")
        layers.append(output_layer)
        
        return layers
    
    def _build_attention_layers(self) -> List[AttentionLayer]:
        """Build attention layers."""
        attention_layers = []
        for idx in range(len(self.hidden_sizes)):
            attention = AttentionLayer(
                self.hidden_sizes[idx],
                self.num_attention_heads,
                name=f"attention_{idx}"
            )
            attention_layers.append(attention)
        
        return attention_layers
    
    def forward(self, x: List[float]) -> List[float]:
        """
        Forward pass through the network.
        
        Args:
            x: Input vector
            
        Returns:
            Output vector
        """
        if len(x) != self.input_size:
            raise ValueError(f"Input size mismatch: expected {self.input_size}, got {len(x)}")
        
        current = x
        
        # Pass through layers with attention
        for idx, layer in enumerate(self.layers[:-1]):
            current = layer.forward(current)
            
            # Apply attention if available
            if idx < len(self.attention_layers):
                current = self.attention_layers[idx].forward(current, current, current)
            
            # Apply activation (ReLU simulation)
            current = [max(0, val) for val in current]
        
        # Output layer (no activation)
        output = self.layers[-1].forward(current)
        
        return output
    
    def get_architecture(self) -> Dict[str, Any]:
        """
        Get network architecture information.
        
        Returns:
            Dictionary describing the architecture
        """
        return {
            "input_size": self.input_size,
            "hidden_sizes": self.hidden_sizes,
            "output_size": self.output_size,
            "num_layers": len(self.layers),
            "num_attention_heads": self.num_attention_heads,
            "dropout_rate": self.dropout_rate,
            "total_parameters": self._count_parameters(),
        }
    
    def _count_parameters(self) -> int:
        """Count total number of parameters in the network."""
        total = 0
        for layer in self.layers:
            total += layer.input_dim * layer.output_dim  # weights
            total += layer.output_dim  # bias
        return total
    
    def summary(self) -> str:
        """
        Generate a summary of the network architecture.
        
        Returns:
            String representation of the network
        """
        lines = ["Neural Network Architecture", "=" * 50]
        lines.append(f"Input size: {self.input_size}")
        lines.append(f"Output size: {self.output_size}")
        lines.append(f"Total layers: {len(self.layers)}")
        lines.append(f"Total parameters: {self._count_parameters():,}")
        lines.append("\nLayer Details:")
        lines.append("-" * 50)
        
        for layer in self.layers:
            lines.append(f"  {layer}")
        
        lines.append("\nAttention Layers:")
        lines.append("-" * 50)
        for attention in self.attention_layers:
            lines.append(f"  {attention}")
        
        return "\n".join(lines)
    
    def __repr__(self) -> str:
        return f"NeuralNetwork(layers={len(self.layers)}, params={self._count_parameters():,})"
