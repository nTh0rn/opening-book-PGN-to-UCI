
<a id="readme-top"></a>
<div align="center">
<h1 align="center">PGN to UCI</h1>

  <p align="center">
    A simple opening-book creator
  </p>

  <p align="center">
<img src="https://nthorn.com/images/chess-engine/pgn-to-uci.png" width="500">
</p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
    </li>
    <li>
      <a href="#getting-started">Getting started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT -->
## About
This program converts the first 8 moves from each game in a PGN to UCI format in a text file, where each game is its own line. This has only ever been tested on PGNs from [pgnmentor.com](https://www.pgnmentor.com/files.html) and was made specifically to be used with the chess engine [Terconari](https://github.com/nTh0rn/chess-engine).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- INSTALLATION -->
## Getting started

### Prerequisites

1. Install Chess and Glob
   ```sh
   pip install Chess
   pip install Glob
   ```

### Installation

1. Clone/download the repo
   ```sh
   git clone https://github.com/nTh0rn/opening-book-PGN-to-UCI.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage
1. Place all PGNs inside a folder titled "PGNs" in same directory as PGN-to-UCI.py.
2. Execute PGN-to-UCI.py.
3. The output will be created in a text document UCI.txt in the same directory as PGN-to-UCI.py.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Nikolas Thornton - [nthorn.com](https://nthorn.com) - contact@nthorn.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>

