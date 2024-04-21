class BranchSaver():
    branch_list = []

    @classmethod
    def save_branch(cls, branch):
        cls.branch_list.append(branch)
        print('\n*** OK! Your Branch Successfully Added.')

    @classmethod
    def print_info(cls):
        for branch in cls.branch_list:
            branch.show_details()