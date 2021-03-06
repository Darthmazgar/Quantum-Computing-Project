    # This only works on three qubits, as n_qubits became seriously hard to make (large number of gates, need to be able to reverse gates etc.)


def invft(register):
        gate1 = H % I(2)
        gate2 = CUGate(base=np.array([1,0],[0,i]),n_control=1,empty_qw=0,reverse=True) % I(1)
        gate3 = CUGate(base=np.array([1,0],[0,(np.sqrt(2)/2 + np.sqrt(2)*j)/2]),n_control=1,empty_qw = 1,reverse = True)
        gate4 = I(1) % H % I(1)
        gate5 = I(1) % CUGate(base=np.array([1,0],[0,i]),n_control=1,empty_qw=0,reverse=True)
        gate6 = I(2) % H
        gate = gate1 * gate2 * gate3 * gate4 * gate5 * gate6
        gate.transpose()
        return gate
