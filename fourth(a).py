current_drugs = {'Paracetamol', 'Ibuprofen', 'Aspirin'}
allergic_drugs = {'Aspirin', 'Penicillin'}
interaction_pairs = {('Ibuprofen', 'Aspirin'), ('Paracetamol', 'Warfarin')}
allergic_reactions = current_drugs.intersection(allergic_drugs)

if allergic_reactions:
    print(f"Warning: The patient is allergic to the following drug(s): {allergic_reactions}")
else:
    print("No known allergies to the current drugs.")

interactions = set()

for drug1 in current_drugs:
    for drug2 in current_drugs:
        if drug1 != drug2 and (drug1, drug2) in interaction_pairs:
            interactions.add((drug1, drug2))

if interactions:
    print(f"Warning: The following drugs have interactions: {interactions}")
else:
    print("No known drug interactions in the current medication list.")
