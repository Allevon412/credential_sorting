# credential_sorting
This python script is used to sort through cracked credentials from an NTDS dump generated using secrets dump.


Very simple script used to take SECRETSDUMP NTDS output (ntds_hashes) and cracked hashes file (cracked_hashes) in the format hash:password sort them and associate them with each enabled user found in the NTDS file. Then it will create a new file specified by sorted_creds and write the credentials in the format username:password to the new file.
