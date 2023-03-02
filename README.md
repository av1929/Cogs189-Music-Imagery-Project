# Decoding Music Imagery With OpenBCI Cyton

Our goal is to evaluate whether the cyton’s limited channel count and radio pipeline is capable of recording EEG data with sufficient resolution and timing accuracy for successful decoding of music imagery. From office hour discussions, we can target successful decoding of imagery onsets (for example, the timing of imagined drum hits), where the start of an imagery trial could be cued via audible metronome clicks. If we are unable to get clean imagery signals, we could perhaps target an N400 surprise for altered musical stimuli instead.

# Stimuli Generation
Stimuli are metronome and snare / kick patterns generated using Ableton.

The two parameters being controlled varied across trials are the:
- sound, and 
- timing of each note (event).

## Sound

## Timing
Syncopated MIDI timings are from [GrFNNRhythm](https://github.com/MusicDynamicsLab/GrFNNRhythm) (included here as a submodule). See the missing pulse paper for more information:

Tal, I., Large, E. W., Rabinovitch, E., Wei, Y., Schroeder, C. E., Poeppel, D., & Golumbic, E. Z. (2017). Neural Entrainment to the Beat: The “Missing-Pulse” Phenomenon. Journal of Neuroscience, 37(26), 6331–6341. https://doi.org/10.1523/JNEUROSCI.2500-16.2017

File | Tal et. al. | exp0
:-- | :-: | :-: |
[comp0p1](stim/GrFNNRhythm/comp0p1.mid) | isochronous | ✓
[comp4p1](stim/GrFNNRhythm/comp4p1.mid) | mp1         | ✓
[comp4p2](stim/GrFNNRhythm/comp4p2.mid) | mp2         | ✓
[comp4p3](stim/GrFNNRhythm/comp4p3.mid) | unused      |

# Stimulus Presentation Setup (PsychoPy)
Stimuli are presented using psychopy.
If using the GUI, a standalone installation might be easiest to use:
https://www.psychopy.org/download.html

If using the coder mode, psychopy could be installed using pip3 / conda:
https://www.psychopy.org/download.html#pip-install

However, it is not clear if the pip install would get all the dependencies to allow running the psychopy GUI from command line as well...

# Data Collection Setup (Cyton)
COGS189 [lab protocol](https://docs.google.com/document/d/1Pjg0_rnC3XclhfnZGzFc2k7ZZ2gnczNOgZZR7f-5MEM/edit?usp=sharing)

## External Triggering

## LSL Triggering

# List of Experiments
Experiment        | #Subjects | Psychopy  | Metronome | Listening | Imagery | Tapping |
:--               | :-:       | :-:       | :-: | :-: | :-: | :-: |
[exp0](data/exp0)[^1] | 2         | [...SixTrials.psyexp](stim/Listening_experiment_randomizeInSixTrials.psyexp) | ✓ | ✓ |   |   |
exp0.1            | 2         |           | ✓ | ✓ |   |   |
exp1              | 4         |           | ✓ | ✓ | ✓ |   |
exp2              | 4         |           | ✓ | ✓ | ✓ | ✓ |

[^1] Note that the first subject's experiment was terminated before completion (laptop died), so the total number of trials would be lesser.

# Analysis Pipeline

1. Bandpass filter
2. Eye blinks
3. Epoching
4. Classifier

# Live Demo Widget
