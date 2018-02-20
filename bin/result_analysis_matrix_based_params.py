file_h = './step2/imputation.step2.hd5'
file_h_ori = 'cell_row'  # gene_row/cell_row

file_x = '../data/gtex_v7.count.4tissues.msk90.hd5'
file_x_ori = 'cell_row'

file_m = '../data/gtex_v7.count.4tissues_yes.hd5'
file_m_ori = 'cell_row'

tag = 'GTex_NonOverlap_4tissues_CountLog_Msk90_TransLate_5L'

data_transformation = 'log'  # as_is/log/rpm_log/exp_rpm_log (done on H, X, M)

# Gene list
pair_list = [
    # # MBM: Cd34, Gypa, Klf1, Sfpi1
    # [4058, 7496],
    # [8495, 12871],
    #
    # TEST
    [2, 3],

    # # PBMC G5561 Non-Linear
    # ['ENSG00000173372',
    # 'ENSG00000087086'],
    #
    # ['ENSG00000231389',
    # 'ENSG00000090382'],
    #
    # ['ENSG00000158869',
    # 'ENSG00000090382'],
    #
    # ['ENSG00000074800',
    # 'ENSG00000019582'],
    #
    # ['ENSG00000157873',
    # 'ENSG00000169583'],
    #
    # ['ENSG00000065978',
    # 'ENSG00000139193'],
    #
    # ['ENSG00000117450',
    # 'ENSG00000133112'],
    #
    # ['ENSG00000155366',
    # 'ENSG00000167996'],


]

gene_list = [
    # # MBM
    # 4058, 7496, 8495, 12871,

    # TEST
    2, 3,
    # 'ENSG00000188976', 'ENSG00000188290',

    # # PBMC G5561 Non-Linear
    # 'ENSG00000173372',
    # 'ENSG00000087086',
    #
    # 'ENSG00000231389',
    # 'ENSG00000090382',
    #
    # 'ENSG00000158869',
    # 'ENSG00000090382',
    #
    # 'ENSG00000074800',
    # 'ENSG00000019582',
    #
    # 'ENSG00000157873',
    # 'ENSG00000169583',
    #
    # 'ENSG00000065978',
    # 'ENSG00000139193',
    #
    # 'ENSG00000117450',
    # 'ENSG00000133112',
    #
    # 'ENSG00000155366',
    # 'ENSG00000167996',

]
