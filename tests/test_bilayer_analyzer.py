from vorbilt.bilayer_analyzer.bilayer_analyzer import BilayerAnalyzer
from vorbilt.bilayer_analyzer.analysis_protocols import valid_analysis

#define tests

#input options
def test_input_options():
    #initialize analyzer with keyword options--and default analysis
    sel_string = "not resname CLA and not resname TIP3 and not resname POT"
    ba = BilayerAnalyzer(
        psf_file='../vorbilt/sample_bilayer/sample_bilayer.psf',
        trajectory='../vorbilt/sample_bilayer/sample_bilayer_10frames.dcd',
        selection=sel_string,
    )
    #add analysis by string input
    ba.add_analysis('msd msd_2 leaflet upper resname POPC')
    #add plot by string -- currenlty only available
    ba.add_plot('msd msd_p msd_1 DOPE-U msd_2 POPC-U')
    #add analysis by list/tuple input
    ba.add_analysis(['msd', 'msd_3', {'resname': 'POPC', 'leaflet': 'lower'}])
    #add analysis by dictionary input
    analysis_in_dict = dict()
    analysis_in_dict['analysis_key'] = 'msd'
    analysis_in_dict['analysis_id'] = 'msd_4'
    analysis_in_dict['analysis_settings'] = {'resname': 'DOPE', 'leaflet': 'lower'}
    ba.add_analysis(analysis_in_dict)
    # run the analyses
    ba.run_analysis()
    #initialize analyzer using input script
    ba = BilayerAnalyzer(input_file='sample_1.in')
    #run analysis
    ba.run_analysis()

#analsyses with default options
def test_analysis_defaults():
    sel_string = "not resname CLA and not resname TIP3 and not resname POT"
    ba = BilayerAnalyzer(
        psf_file='../vorbilt/sample_bilayer/sample_bilayer.psf',
        trajectory='../vorbilt/sample_bilayer/sample_bilayer_10frames.dcd',
        selection=sel_string,
    )
    for key in valid_analysis:
        analysis_in = [key, key+"_t", dict()]
        ba.add_analysis(analysis_in)
    ba.print_analysis_protocol()
    ba.run_analysis()
    print("outputs:")
    for key in valid_analysis:
        a_id = key+"_t"
        print(a_id+":")
        print(ba.get_analysis_data(a_id))


test_input_options()
test_analysis_defaults()