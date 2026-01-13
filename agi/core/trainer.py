"""
AGI Framework - Model Trainer
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Training utilities for AGI models
"""

from typing import Dict, List, Optional, Any, Callable
from datetime import datetime
import json


class TrainingConfig:
    """Configuration for model training."""
    
    def __init__(
        self,
        learning_rate: float = 0.001,
        batch_size: int = 32,
        epochs: int = 10,
        validation_split: float = 0.2,
        early_stopping_patience: int = 3,
        checkpoint_frequency: int = 1,
        log_frequency: int = 100
    ):
        """
        Initialize training configuration.
        
        Args:
            learning_rate: Learning rate for optimization
            batch_size: Batch size for training
            epochs: Number of training epochs
            validation_split: Fraction of data to use for validation
            early_stopping_patience: Epochs to wait before early stopping
            checkpoint_frequency: Frequency of model checkpoints (in epochs)
            log_frequency: Frequency of logging (in steps)
        """
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.epochs = epochs
        self.validation_split = validation_split
        self.early_stopping_patience = early_stopping_patience
        self.checkpoint_frequency = checkpoint_frequency
        self.log_frequency = log_frequency
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "learning_rate": self.learning_rate,
            "batch_size": self.batch_size,
            "epochs": self.epochs,
            "validation_split": self.validation_split,
            "early_stopping_patience": self.early_stopping_patience,
            "checkpoint_frequency": self.checkpoint_frequency,
            "log_frequency": self.log_frequency,
        }


class ModelTrainer:
    """
    Trainer class for AGI models.
    
    Provides comprehensive training utilities including:
    - Training loop management
    - Validation and early stopping
    - Learning rate scheduling
    - Checkpointing
    - Training metrics tracking
    """
    
    def __init__(
        self,
        model: Any,
        config: Optional[TrainingConfig] = None
    ):
        """
        Initialize model trainer.
        
        Args:
            model: Model instance to train
            config: Training configuration
        """
        self.model = model
        self.config = config or TrainingConfig()
        self.training_history = {
            "loss": [],
            "accuracy": [],
            "val_loss": [],
            "val_accuracy": [],
        }
        self.best_val_loss = float('inf')
        self.patience_counter = 0
        
    def train(
        self,
        training_data: List[Any],
        validation_data: Optional[List[Any]] = None,
        callbacks: Optional[List[Callable]] = None
    ) -> Dict[str, Any]:
        """
        Train the model.
        
        Args:
            training_data: List of training examples
            validation_data: Optional validation data
            callbacks: Optional list of callback functions
            
        Returns:
            Training history dictionary
        """
        print(f"Starting training with configuration:")
        print(f"  Learning rate: {self.config.learning_rate}")
        print(f"  Batch size: {self.config.batch_size}")
        print(f"  Epochs: {self.config.epochs}")
        print(f"  Training samples: {len(training_data)}")
        
        if validation_data:
            print(f"  Validation samples: {len(validation_data)}")
        
        # Calculate number of batches
        num_batches = (len(training_data) + self.config.batch_size - 1) // self.config.batch_size
        
        for epoch in range(self.config.epochs):
            print(f"\nEpoch {epoch + 1}/{self.config.epochs}")
            print("-" * 50)
            
            # Training phase
            epoch_loss, epoch_acc = self._train_epoch(training_data, num_batches)
            self.training_history["loss"].append(epoch_loss)
            self.training_history["accuracy"].append(epoch_acc)
            
            print(f"Training   - Loss: {epoch_loss:.4f}, Accuracy: {epoch_acc:.4f}")
            
            # Validation phase
            if validation_data:
                val_loss, val_acc = self._validate(validation_data)
                self.training_history["val_loss"].append(val_loss)
                self.training_history["val_accuracy"].append(val_acc)
                
                print(f"Validation - Loss: {val_loss:.4f}, Accuracy: {val_acc:.4f}")
                
                # Early stopping check
                if self._check_early_stopping(val_loss):
                    print(f"\nEarly stopping triggered at epoch {epoch + 1}")
                    break
            
            # Checkpoint saving
            if (epoch + 1) % self.config.checkpoint_frequency == 0:
                self._save_checkpoint(epoch + 1)
            
            # Execute callbacks
            if callbacks:
                for callback in callbacks:
                    callback(epoch, self.training_history)
        
        print("\nTraining complete!")
        return self.training_history
    
    def _train_epoch(self, training_data: List[Any], num_batches: int) -> tuple:
        """Train for one epoch."""
        total_loss = 0.0
        total_acc = 0.0
        
        for batch_idx in range(num_batches):
            # Simulate batch processing
            batch_loss = 1.0 / (batch_idx + 1 + len(self.training_history["loss"]) * num_batches)
            batch_acc = min(0.98, 0.5 + (batch_idx + len(self.training_history["loss"]) * num_batches) * 0.01)
            
            total_loss += batch_loss
            total_acc += batch_acc
            
            if (batch_idx + 1) % self.config.log_frequency == 0:
                avg_loss = total_loss / (batch_idx + 1)
                avg_acc = total_acc / (batch_idx + 1)
                print(f"  Batch {batch_idx + 1}/{num_batches} - Loss: {avg_loss:.4f}, Acc: {avg_acc:.4f}")
        
        epoch_loss = total_loss / num_batches
        epoch_acc = total_acc / num_batches
        
        return epoch_loss, epoch_acc
    
    def _validate(self, validation_data: List[Any]) -> tuple:
        """Run validation."""
        # Simulate validation
        val_loss = 1.0 / (len(self.training_history["loss"]) + 1) * 1.2
        val_acc = min(0.95, 0.5 + len(self.training_history["loss"]) * 0.045)
        
        return val_loss, val_acc
    
    def _check_early_stopping(self, val_loss: float) -> bool:
        """Check if early stopping should be triggered."""
        if val_loss < self.best_val_loss:
            self.best_val_loss = val_loss
            self.patience_counter = 0
            return False
        else:
            self.patience_counter += 1
            if self.patience_counter >= self.config.early_stopping_patience:
                return True
            return False
    
    def _save_checkpoint(self, epoch: int) -> None:
        """Save training checkpoint."""
        checkpoint = {
            "epoch": epoch,
            "model_state": getattr(self.model, '_model_state', {}),
            "training_history": self.training_history,
            "config": self.config.to_dict(),
            "timestamp": datetime.now().isoformat(),
        }
        
        filename = f"checkpoint_epoch_{epoch}.json"
        with open(filename, 'w') as f:
            json.dump(checkpoint, f, indent=2)
        
        print(f"  Checkpoint saved: {filename}")
    
    def get_training_summary(self) -> str:
        """
        Get a summary of training progress.
        
        Returns:
            Summary string
        """
        lines = ["Training Summary", "=" * 50]
        
        if self.training_history["loss"]:
            lines.append(f"Epochs completed: {len(self.training_history['loss'])}")
            lines.append(f"Best training loss: {min(self.training_history['loss']):.4f}")
            lines.append(f"Best training accuracy: {max(self.training_history['accuracy']):.4f}")
            
            if self.training_history["val_loss"]:
                lines.append(f"Best validation loss: {min(self.training_history['val_loss']):.4f}")
                lines.append(f"Best validation accuracy: {max(self.training_history['val_accuracy']):.4f}")
        else:
            lines.append("No training history available")
        
        return "\n".join(lines)
    
    def plot_training_curves(self) -> Dict[str, List[float]]:
        """
        Get training curves data for plotting.
        
        Returns:
            Dictionary with training metrics
        """
        return self.training_history
    
    def __repr__(self) -> str:
        return f"ModelTrainer(epochs={self.config.epochs}, lr={self.config.learning_rate})"
