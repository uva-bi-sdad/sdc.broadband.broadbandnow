import pathlib
import pandas as pd
from tqdm import tqdm
from datetime import datetime

if __name__ == "__main__":
    pbar = tqdm(
        sorted(
            [
                p
                for p in list(pathlib.Path("../../data/").glob("*.csv.xz"))
                if p.is_file()
            ]
        )
    )
    for path in pbar:
        df = pd.read_csv(path, dtype={"GEOID20": object})
        # print(df.dtypes)
        df = df[df["GEOID20"].notnull()]
        df["len"] = df["GEOID20"].map(len)
        df = df[df["len"] >= 14]  # remove fips under 14 chracters
        df["GEOID20"] = df["GEOID20"].apply(lambda x: x.zfill(15))

        # df["year_parsed"] = datetime.now().strftime("%Y")
        pbar.set_description("Updating: %s" % path)

        assert all(df["GEOID20"].str[:5].unique() == path.name[:5])
        df = df[
            [
                "speed",
                "down_up",
                "price",
                "name",
                "type",
                "address",
                "GEOID20",
                "longitude",
                "latitude",
                "year_parsed",
            ]
        ]
        assert list(df.columns) == [
            "speed",
            "down_up",
            "price",
            "name",
            "type",
            "address",
            "GEOID20",
            "longitude",
            "latitude",
            "year_parsed",
        ]
        df.to_csv(path, index=False)
