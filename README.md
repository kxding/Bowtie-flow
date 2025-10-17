# Bowtie-flow: Efficient High-Resolution Video Generation with Prior Preservation



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




## ⚙️ Gallery

### Comparison
- [720p Video](comparison/720p.mp4)
- [1080p Video](comparison/1080p.mp4)


## Citation

<!-- ```bibtex
 @article{cai2025videocanvas,
    title={VideoCanvas: Unified Video Completion from Arbitrary Spatiotemporal Patches via In-Context Conditioning},
    author={Minghong Cai, Qiulin Wang, Zongli Ye, Wenze Liu, Quande Liu, Weicai Ye, Xintao Wang, Pengfei Wan, Kun Gai, Xiangyu Yue},
    journal={arXiv preprint arXiv:2510.08555},
    year={2025}
} -->
