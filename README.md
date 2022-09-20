# ADV_Bio_DYO
	
This repository contains phylogenetic analyses of coelecanth, lungfish, tetrapods, and other related species using hemoglobin protein sequences, which I did as a final project for my highschool biology class. Here's a quick summary:

Approximately 370 million years ago, a bony-fish waddled onto land for the first time. This fish, or a relative, would become the common ancestor for all land-dwelling vertebrates, including dinosaurs, mammals, and snakes. To understand macroevolution, it is crucial to understand the details of this jump to land, as it acted as a bottleneck in determining the morphology of land-dwelling animals. The lobe-finned fish, bony fish which diverged from ray-finned fish, are a clade that includes the sea-land transition fish, but also includes Lungfish and Coelacanths, two potential sister species with tetrapods who dwell in the ocean to this day.

A previous study analyzing hemoglobin primary structure suggested that Coelacanth is the sister species of tetrapods, but morphological similarities suggest that lungfish are closer ([Gorr et al.](https://pubmed.ncbi.nlm.nih.gov/1958318/)). The goal of this lab was to analyze Hemoglobin sequences from Tetrapods, Coelacanth, and Lungfish, to determine whether Coelacanth or Lungfish share a more recent common ancestor with tetrapods. This will shed light on the morphology of the first land-dwelling vertebrate, whose identity has not been determined.

We attempted to sequence hemoglobin of extant ray-finned fishes, cod and salmon, using primers from Borza et. al. DNA extraction failed, and so public sequences were used to preform the analysis. DNA was extracted by macerating fish meat, adding the meat to phosphate buffered saline (PBS) and instagene matrix, vortexing, heating, and then centrifuging. Primers were added to 2ul of purified DNA and a pure-taq PCR bead, then placed in a PCR heat-cycler. PCR product was analyzed using gel electrophoresis. Because we did not get any PCR hits, we conducted DNA barcoding on the purified DNA. A gel of the barcoding product did not have a band in the expected 500-600 bp range, so DNA extraction may have failed. 

We next gathered 200 hemoglobin sequences from both HBA and HBB from Uniprot. Sequences were compared using BioPyhton, and raw identity and BLOSUM62 algorithms. 

Identity between lungfish and tetrapod sequences was higher than identity between coelacanth and tetrapod, (0.879 and 0.73 for HBA, raw comparison), suggesting that lungfish are the sister species of tetrapods over coelacanth.
