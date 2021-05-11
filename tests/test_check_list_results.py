import check_analyses as ca


def test_are_results_in_alphabetical_order():
    assert ca.are_results_in_alphabetical_order("primer_reporte")
    assert not ca.are_results_in_alphabetical_order("segundo_reporte")
