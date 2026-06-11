---
tags: [diffusion-models, mathematics, ai, deep-learning]
status: complete
created: 2026-06-10
---

# Diffusion Models Mathematics

## 1. The Generative Framework
Diffusion models are based on the concept of adding Gaussian noise to data and then learning to reverse that process to recover the original signal.

### The Forward Diffusion Process ($q$)
The forward process gradually adds noise to the data $x_0$ over $T$ steps.
$$q(x_t | x_{t-1}) = \mathcal{N}(x_t; \sqrt{1 - \beta_t}x_{t-1}, \beta_t \mathbf{I})$$
Where $\beta_t$ is a variance schedule. Using the reparameterization trick, we can sample $x_t$ directly from $x_0$:
$$x_t = \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1 - \bar{\alpha}_t}\epsilon, \quad \epsilon \sim \mathcal{N}(0, \mathbf{I})$$
where $\alpha_t = 1 - \beta_t$ and $\bar{\alpha}_t = \prod_{i=1}^t \alpha_i$.

### The Reverse Diffusion Process ($p_\theta$)
The goal is to learn a model $p_\theta(x_{t-1} | x_t)$ that approximates the reverse of the forward process.
$$p_\theta(x_{t-1} | x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$$
The model $\theta$ is trained to predict the noise $\epsilon$ that was added to $x_0$ to reach $x_t$.

## 2. Architecture: The U-Net
The core of the reverse process is typically a **U-Net** architecture.
- **Encoder:** Downsamples the noisy image using convolutional layers and pooling, extracting high-level semantic features.
- **Bottleneck:** The deepest part of the network where the most abstract representation exists.
- **Decoder:** Upsamples the representation back to the original image resolution.
- **Skip Connections:** Connect encoder layers to corresponding decoder layers, preserving spatial information (crucial for reconstructing fine details).
- **Time Embeddings:** Since the noise level varies by $t$, the time step is encoded as a vector and added to the U-Net's intermediate layers.

## 3. Score-Based Modeling
Diffusion can be viewed as learning the gradient of the log-density of the data distribution (the **Score Function**).
$$\text{Score} = \nabla_x \log p(x)$$
The reverse process is essentially performing **Langevin Dynamics**, moving the noisy sample along the gradient of the score function to regions of higher probability (the original data manifold).

## 4. Latent Diffusion Models (LDM)
Standard diffusion on high-resolution pixels is computationally expensive. LDM (the basis for Stable Diffusion) solves this by operating in a compressed **latent space**.

### Components:
1. **Variational Autoencoder (VAE):** 
   - **Encoder $\mathcal{E}$:** Maps image $x \in \mathbb{R}^{H \times W \times 3}$ to latent $z \in \mathbb{R}^{h \times w \times c}$.
   - **Decoder $\mathcal{D}$:** Reconstructs the image from the latent space.
2. **Diffusion Model in Latent Space:** The diffusion process happens on $z$ instead of $x$.
3. **Conditioning (Cross-Attention):** To guide generation (e.g., text-to-image), conditioning information $y$ (from a CLIP text encoder) is injected into the U-Net using cross-attention layers.

## 5. Summary of the LDM Workflow
$\text{Text Prompt} \xrightarrow{\text{CLIP}} \text{Embeddings} \xrightarrow{\text{U-Net (Reverse Diffusion in } z\text{-space)}} \text{Latent } z_0 \xrightarrow{\text{VAE Decoder}} \text{Image } x_0$

---
**Related Notes:**
- [[Modelos-de-Linguagem-LLMs]]
- [[Embeddings-e-Busca-Semantica]]
