class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title=None):
        if title:
            print(title)

        n_cols = df.shape[1]
        n_rows = df.shape[0]
        n_duplicates = df.duplicated().sum()
        duplicate_share = n_duplicates / n_rows

        print(f'Количество столбцов: {n_cols}')
        print(f'Количество строк: {n_rows}')
        print(f'Количество дубликатов: {n_duplicates}')
        print(f'Доля дубликатов: {format(duplicate_share, self.percent_format)}')

        if self.include_all:
            print(df.describe(include='all'))
        else:
            print(df.describe())

        print('Количество пропусков:', df.isna().sum().sum())
        print('Доля пропусков:', format(df.isna().mean().mean(), self.float_format))
