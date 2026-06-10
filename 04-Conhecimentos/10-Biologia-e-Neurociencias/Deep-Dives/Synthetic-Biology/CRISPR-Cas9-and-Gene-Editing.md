---
category: Synthetic Biology
tags: [CRISPR, Gene Editing, Biotechnology]
links: [[05-Psicologia-e-Cognicao]]
---

# CRISPR-Cas9 and Gene Editing

## Mecanismo de Ação e Clivagem Molecular
O sistema CRISPR-Cas9 opera através de um mecanismo de *RNA-guided endonuclease*. A precisão do sistema depende da formação de um complexo entre a proteína Cas9 e um *single-guide RNA (sgRNA)*. O sgRNA é composto por um *crRNA (CRISPR RNA)*, que define a especificidade da sequência alvo, e um *tracrRNA (trans-activating CRISPR RNA)*, que recruta a nuclease.

A Cas9 escaneia o DNA em busca da *Protospacer Adjacent Motif (PAM)*, geralmente 5'-NGG-3'. Uma vez reconhecida a PAM, ocorre a hibridização do sgRNA com a fita complementar do DNA, induzindo uma *Double-Strand Break (DSB)* exatamente três nucleotídeos a montante da PAM.

## Vias de Reparo Celular
Após a clivagem, a célula tenta reparar a quebra via:
1. **Non-Homologous End Joining (NHEJ)**: Um processo propenso a erros que frequentemente resulta em *Indels (Insertions and Deletions)*, levando ao *gene knockout* por *frameshift mutations*.
2. **Homology-Directed Repair (HDR)**: Um mecanismo de alta precisão que utiliza um *donor template* de DNA exógeno para realizar *precise gene insertion* ou substituição de bases específicas.

## Off-target Effects e Especificidade
Um dos maiores desafios reside nos *off-target effects*, onde a Cas9 cliva sequências de DNA com similaridade parcial ao guia. Isso pode levar a *genomic instability* e mutações deletérias em loci não pretendidos. Estratégias de mitigação incluem o uso de *High-Fidelity Cas9 variants* (como eSpCas9 ou Cas9-HF1) e *Base Editing* ou *Prime Editing*, que permitem a alteração de nucleotídeos sem a necessidade de *Double-Strand Breaks*.

## Germline Editing e Implicações Futuras
A edição de *germline cells* (gametas e zigotos) implica que as alterações sejam herdáveis. A transição do *Somatic Gene Therapy* para o *Germline Editing* levanta questões críticas sobre a *genetic enhancement* e o risco de *off-target mutations* permanentes na linhagem humana. O futuro aponta para a integração de *Epigenome Editing*, onde a expressão gênica é modulada via *CRISPRi (interference)* ou *CRISPRa (activation)* sem alterar a sequência primária do DNA.
