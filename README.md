# SDU_ECDSA

PoC impl of the following pitfall:  
• Leaking 𝑘 leads to leaking of 𝑑   
• Reusing 𝑘 leads to leaking of 𝑑  
• Two users, using 𝑘 leads to leaking of 𝑑, that is they can deduce each other’s 𝑑 • Malleability of ECDSA, e.g. 𝑟, 𝑠 and 𝑟,−𝑠 are both valid 
signatures  
• Pretend to be satoshi as one can forge signature if the verification does not check 𝑚 • Same 𝑑 and 𝑘 used in ECDSA & Schnorr signature, leads to 
leaking of 𝑑  

# Implementation
## Implement ECDSA signature:   
## Achieve ECDSA certification:
