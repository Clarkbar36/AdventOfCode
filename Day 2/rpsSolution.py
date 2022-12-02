import pandas as pd
import numpy as np

elf_encrpyted_guide = pd.read_csv('C:/Users/aclark5/PycharmProjects/AdventOfCode/Day 2/d2_data.txt', sep=" ", header=None)
elf_encrpyted_guide.columns = ["opponent", "self"]

elf_encrpyted_guide["opponent_play"] = np.where(elf_encrpyted_guide["opponent"] == 'A', 'Rock',
                                 np.where(elf_encrpyted_guide["opponent"] == 'B', 'Paper',
                                 np.where(elf_encrpyted_guide["opponent"] == 'C', 'Scissor', 'NULL')))

elf_encrpyted_guide["self_play"] = np.where(elf_encrpyted_guide["self"] == 'X', 'Rock',
                                 np.where(elf_encrpyted_guide["self"] == 'Y', 'Paper',
                                 np.where(elf_encrpyted_guide["self"] == 'Z', 'Scissor', 'NULL')))

elf_encrpyted_guide["self_score"] = np.where(elf_encrpyted_guide["self"] == 'X', 1,
                                 np.where(elf_encrpyted_guide["self"] == 'Y', 2,
                                 np.where(elf_encrpyted_guide["self"] == 'Z', 3, 0)))

elf_encrpyted_guide["result"] =np.where((elf_encrpyted_guide["self_play"] == 'Rock') & (elf_encrpyted_guide["opponent_play"] == 'Scissor'), 6,
                            np.where((elf_encrpyted_guide["self_play"] == 'Rock') & (elf_encrpyted_guide["opponent_play"] == 'Paper'), 0,
                            np.where((elf_encrpyted_guide["self_play"] == 'Paper') & (elf_encrpyted_guide["opponent_play"] == 'Rock'), 6,
                            np.where((elf_encrpyted_guide["self_play"] == 'Paper') & (elf_encrpyted_guide["opponent_play"] == 'Scissor'), 0,
                            np.where((elf_encrpyted_guide["self_play"] == 'Scissor') & (elf_encrpyted_guide["opponent_play"] == 'Paper'), 6,
                            np.where((elf_encrpyted_guide["self_play"] == 'Scissor') & (elf_encrpyted_guide["opponent_play"] == 'Rock'), 0, 3
                                     ))))))
elf_encrpyted_guide["score"] = elf_encrpyted_guide["self_score"] + elf_encrpyted_guide["result"]

elf_encrpyted_guide["score"].sum()

elf_encrpyted_guide["expected_result"] = np.where(elf_encrpyted_guide["self"] == 'X', 'Lose',
                                        np.where(elf_encrpyted_guide["self"] == 'Y', 'Draw',
                                        np.where(elf_encrpyted_guide["self"] == 'Z', 'Win', 'NULL')))

elf_encrpyted_guide["expected_result_score"] = np.where(elf_encrpyted_guide["self"] == 'X', 0,
                                        np.where(elf_encrpyted_guide["self"] == 'Y', 3,
                                        np.where(elf_encrpyted_guide["self"] == 'Z', 6, 99)))

elf_encrpyted_guide["new_self_play"] = np.where((elf_encrpyted_guide["expected_result"] == 'Lose') & (elf_encrpyted_guide["opponent_play"] == 'Rock'), "Scissor",
                                       np.where((elf_encrpyted_guide["expected_result"] == 'Lose') & (elf_encrpyted_guide["opponent_play"] == 'Paper'), "Rock",
                                       np.where((elf_encrpyted_guide["expected_result"] == 'Lose') & (elf_encrpyted_guide["opponent_play"] == 'Scissor'), "Paper",
                                       np.where((elf_encrpyted_guide["expected_result"] == 'Win') & (elf_encrpyted_guide["opponent_play"] == 'Rock'), "Paper",
                                       np.where((elf_encrpyted_guide["expected_result"] == 'Win') & (elf_encrpyted_guide["opponent_play"] == 'Paper'), "Scissor",
                                       np.where((elf_encrpyted_guide["expected_result"] == 'Win') & (elf_encrpyted_guide["opponent_play"] == 'Scissor'), "Rock",
                                       elf_encrpyted_guide["opponent_play"]))))))

elf_encrpyted_guide["new_self_score"] = np.where(elf_encrpyted_guide["new_self_play"] == 'Rock', 1,
                                 np.where(elf_encrpyted_guide["new_self_play"] == 'Paper', 2,
                                 np.where(elf_encrpyted_guide["new_self_play"] == 'Scissor', 3, 0)))

elf_encrpyted_guide["new_score"] = elf_encrpyted_guide["new_self_score"] + elf_encrpyted_guide["expected_result_score"]

elf_encrpyted_guide["new_score"].sum()