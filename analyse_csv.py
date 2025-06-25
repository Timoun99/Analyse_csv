import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Analyse de fichiers CSV métiers")
parser.add_argument("--fichier", required=True, help="Chemin vers le fichier CSV")
parser.add_argument("--ville", help="Filtrer par ville")
parser.add_argument("--tri", help="Nom de la colonne à trier")
args = parser.parse_args()

df = pd.read_csv(args.fichier)

if args.ville:
    df = df[df['ville'] == args.ville]

if args.tri:
    df = df.sort_values(by=args.tri)

print(df.head())