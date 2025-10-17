# Bowtie-flow: Efficient High-Resolution Video Generation with Prior Preservation


https://github.com/user-attachments/assets/cec0d342-5af0-4d05-a623-1f5a33729183


**[Kaixin Ding<sup>1 &dagger;</sup>](https://your-link-to-kaixin), 
[Xi Chen<sup>1</sup>](https://your-link-to-xi-chen), 
[Sihui Ji<sup>1</sup>](https://your-link-to-sihui-ji), 
[Yuan Gao<sup>2</sup>](https://your-link-to-yuan-gao), 
[Liang Hou<sup>2</sup>](https://your-link-to-liang-hou), 
[Xin Tao<sup>2</sup>](https://your-link-to-xin-tao), 
[Pengfei Wan<sup>2</sup>](https://your-link-to-pengfei-wan), 
[Hengshuang Zhao<sup>1 &#9993;</sup>](https://your-link-to-hengshuang-zhao)**
<br>
<sup>1</sup>The University of Hong Kong  
<sup>2</sup>Kling Team, Kuaishou Technology  
<br>
&dagger;: Intern at Kling Team, KuaishouTechnology, &#9993;: Corresponding Author

<a href='https://kxding.github.io/project/Bowtie-flow/'><img src='https://img.shields.io/badge/ArXiv-2510.08555-red'></a> 
<a href='https://kxding.github.io/project/Bowtie-flow/#'><img src='https://img.shields.io/badge/Project-Page-Green'></a>





## 📋 News
- [2025.10.14] Release Arxiv paper.


## 📖 Introduction
High-resolution video generation is slow: for example, Wan 2.1 takes over 50 minutes to generate a 720p video. Existing acceleration methods often compromise model priors (layout, semantics, motion). We propose Bowtie-flow, a two-stage framework: first, a fast low-resolution preview using a pretrained model; second, a Refiner to upscale while preserving priors. Key techniques include noise reshifting to reduce prior loss and shifting windows with careful training design. Bowtie-flow is simple, efficient, and compatible with various base models, achieving 12.5× speedup for generating 5-second, 16fps, 720p Wan 2.1 videos and 8.7× speedup for generating 5-second, 24fps, 720p HunyuanVideo.

## 🏆 Quantitative Results

### Comparison on Wan 2.1 14B

| Method      | QS↑   | AQ↑   | DD↑   | MS↑   | OC↑   | SA↑   | PC↑   | Time↓       | Speed↑  | PFLOPs↓ |
|------------|-------|-------|-------|-------|-------|-------|-------|------------|--------|---------|
| Wan 2.1    | 83.31 | 66.9  | 63.89 | 97.65 | 27.08 | 41.82 | 45.45 | 3497 (58min)| 1×     | 658.46  |
| 30% Step   | 77.92 | 58.43 | 56.94 | 96.95 | 24.56 | 18.18 | 16.36 | 1049        | 3.34×  | 197.54  |
| 50% Step   | 81.51 | 63.52 | 66.67 | 96.99 | 25.90 | 25.45 | 23.64 | 1748        | 2×     | 329.23  |
| SVG        | **83.36** | 65.6  | _68.06_ | 97.69 | _27.32_ | 25.45 | 20.00 | 2712       | 1.29×  | 429.86  |
| DMD        | _83.31_ | _66.11_ | 52.78 | **98.96** | 26.77 | _34.55_ | _30.91_ | _282_       | _12.40×_ | _39.51_ |
| Ours       | 83.26 | **66.86** | **72.22** | _97.95_ | **27.38** | **41.82** | **38.18** | **278**     | **12.58×** | **34.3** |



## ⚙️ Gallery

### Comparison
### 720p Video

https://github.com/user-attachments/assets/9fc3640d-f671-419a-9929-b06d77d8411f


### 1080p Video

https://github.com/user-attachments/assets/a50ab7ff-c035-4798-b91c-2dc4e923fc36

### ShowCases
### 720p Video


https://github.com/user-attachments/assets/871729fe-05f6-426d-8e39-504781a2bf10


### 1080p Video


https://github.com/user-attachments/assets/e93330da-9254-4894-a887-deaa3a4f6054


## Citation

<!-- ```bibtex
 @article{cai2025videocanvas,
    title={VideoCanvas: Unified Video Completion from Arbitrary Spatiotemporal Patches via In-Context Conditioning},
    author={Minghong Cai, Qiulin Wang, Zongli Ye, Wenze Liu, Quande Liu, Weicai Ye, Xintao Wang, Pengfei Wan, Kun Gai, Xiangyu Yue},
    journal={arXiv preprint arXiv:2510.08555},
    year={2025}
} -->
