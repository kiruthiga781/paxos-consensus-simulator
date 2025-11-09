import random

class Acceptor:
    def __init__(self, id):
        self.id = id
        self.promised_id = None
        self.accepted_id = None
        self.accepted_value = None

    def prepare(self, proposal_id):
        if not self.promised_id or proposal_id > self.promised_id:
            self.promised_id = proposal_id
            return True, self.accepted_id, self.accepted_value
        return False, self.accepted_id, self.accepted_value

    def accept(self, proposal_id, value):
        if not self.promised_id or proposal_id >= self.promised_id:
            self.promised_id = proposal_id
            self.accepted_id = proposal_id
            self.accepted_value = value
            return True
        return False

class Proposer:
    def __init__(self, id, acceptors):
        self.id = id
        self.acceptors = acceptors
        self.proposal_id = random.randint(1, 100)

    def propose(self, value):
        print(f"\nProposer {self.id} proposing value: {value}")
        promises = []
        for a in self.acceptors:
            ok, aid, aval = a.prepare(self.proposal_id)
            if ok:
                promises.append((aid, aval))
        if len(promises) > len(self.acceptors) // 2:
            print("Majority promised. Sending accept request...")
            success = 0
            for a in self.acceptors:
                if a.accept(self.proposal_id, value):
                    success += 1
            if success > len(self.acceptors) // 2:
                print(f"Value '{value}' chosen by majority.")
            else:
                print("Value not accepted by majority.")
        else:
            print("Majority not achieved. Proposal rejected.")

def simulate_paxos():
    acceptors = [Acceptor(i) for i in range(5)]
    proposer1 = Proposer(1, acceptors)
    proposer2 = Proposer(2, acceptors)

    proposer1.propose("Data_1")
    proposer2.propose("Data_2")

if __name__ == "__main__":
    simulate_paxos()
