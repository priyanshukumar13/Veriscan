# VeriScan: File Safety Scanner
VeriScan is a simple file scanning tool built with Flask that scans files on a user's system to identify potentially harmful ones based on characteristics like file extension, name patterns, and known malware hashes. It helps users determine whether files are "safe" or "unsafe" to open or delete.

![home](https://github.com/user-attachments/assets/cf3f23aa-641a-4eb0-89cb-94e80bd48858)

# Features
- Scans files based on file extensions, size, name (e.g., .exe, .dll, .bat, .vbs).
- Checks file hashes against a list of known malicious hashes.
- Provides a "clean" or "suspicious" status with a message for each file.
- A simple web interface for users to upload files and receive scan results.

# Requirements
- Python 3.x
- Flask
- hashlib

To install the necessary Python dependencies, you can use:
pip install -r requirements.txt

# How It Works
- Suspicious File Extensions: The tool flags files with extensions commonly associated with malicious files (e.g., .exe, .dll, .bat).
- Hash Checking: It compares the file's SHA256 hash against a list of known malicious hashes.
- Response: If a suspicious extension or a known malicious hash is detected, the file is labeled as "suspicious" and flagged as "unsafe". Otherwise, the file is deemed "safe".

# Future Improvements
While VeriScan is designed to detect suspicious files based on known patterns, we plan to enhance the tool in future releases. Upcoming features will include real-time file scanning, cloud-based malware database integration, and more extensive file analysis tools.

# Contributing
We welcome contributions from developers and security enthusiasts. If you have ideas for improvements or want to contribute to VeriScan, feel free to open issues or submit pull requests on GitHub. Please follow the guidelines in the contributing section for submitting code.

# Get Involved
Join the community of developers and cybersecurity experts in improving VerScan and expanding its capabilities. Whether you’re looking to enhance the tool's features, report bugs, or help with documentation, your contributions are always welcome!

# Contact
For any questions, suggestions, or feedback, feel free to reach out to us via email or open an issue on GitHub. We’d love to hear from you!
