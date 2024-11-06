# ML-and-Microplastics
This research introduces an automated approach using machine learning to identify and classify microplastics in water samples from the Boise River Basin.

# Microplastics Detection Using Machine Learning

<img src="/project-icon.png" width="200" height="auto" alt="microplastics-detection-icon"/>

A specialized image detection program that uses TensorFlow for identifying and classifying microplastics in water samples from the Boise River Basin. This project utilizes transfer learning with Google's Inception model to classify different types of microplastics including fibers, beads, films, foam, and fragments.

## Features
- Automated microplastic classification
- Real-time processing capabilities
- Web interface for easy interaction
- Firebase integration for result storage
- Confidence scoring for each classification
- Support for multiple microplastic types

## Requirements
- Python 3.7+
- TensorFlow 2.x
- Flask
- Firebase Admin SDK
- Additional dependencies in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/microplastics-detection.git
cd microplastics-detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the pre-trained Inception model:
```bash
bash setup.sh
```

## Project Structure
```
/
├── training_dataset/
│   ├── beads/
│   ├── fibers/
│   ├── films/
│   ├── foam/
│   ├── fragments/
│   ├── organic/
│   └── undefined/
├── tf_files/
│   ├── retrained_graph.pb
│   └── retrained_labels.txt
├── classify.py
├── retrain.py
├── app.py
└── requirements.txt
```

## Usage

### Training the Model
1. Prepare your dataset in the `training_dataset` folder following the structure above
2. Run the training script:
```bash
bash train.sh
```

### Classification
1. Start the Flask server:
```bash
python app.py
```

2. Use the classifier:
```bash
python classify.py
```

3. Select an image when prompted or use the web interface at `http://localhost:5000`

## Model Architecture
- Base: Inception v3
- Transfer Learning: Modified final layers
- Input size: 299x299 pixels
- Training split: 80% training, 10% validation, 10% testing
- Learning rate: 0.01
- Training steps: 4000

## Performance
- Processing time: ~15-20 seconds per image
- Classification accuracy: ~85-95% (varies by category)
- Supported image formats: JPEG, PNG

## Web Interface
The web interface provides:
- Image upload functionality
- Real-time classification results
- Confidence scores for each category
- Historical data viewing
- Result export options

## API Endpoints
```
POST /detect
- Accepts: Image file (multipart/form-data)
- Returns: JSON with classification results

GET /status
- Returns: Server status
```

## Firebase Integration
Results are automatically stored in Firebase with:
- Timestamp
- Classification results
- Confidence scores
- Image metadata

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Development
- Mobile application development
- Size measurement implementation
- Polymer type identification
- Multi-particle detection
- Real-time monitoring system integration

## Acknowledgments
- The College of Idaho
- M.J. Murdock Charitable Trust Grant #SR202119904
- Boise State University Department of Geosciences

## Research Team
- Suthira de Silva Bathige
- Dr. Rachel Headley
- Department of Environmental Studies, The College of Idaho

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Citation
If you use this project in your research, please cite:
```bibtex
@misc{microplastics-detection,
  author = {de Silva Bathige, Suthira and Headley, Rachel},
  title = {Microplastics Detection Using Machine Learning},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/your-username/microplastics-detection}}
}
```

## Contact
For questions and support, please contact:
- Email: your.email@example.com
- Project Link: https://github.com/your-username/microplastics-detection
