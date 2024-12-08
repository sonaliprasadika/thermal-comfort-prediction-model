try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight=None, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha', 'monotonic_cst'), max_depth=None, max_features=sqrt, max_leaf_nodes=10, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, monotonic_cst=None, n_estimators=20, n_jobs=None, num_outputs=2, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=None, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
    """

    def __init__(self):
        """
        Constructor
        """
        self.latency = 0
        self.predicted_value = -1

        self.votes = [0.00000000000, 0.00000000000]

    def predict(self, x):
        """
        Predict output from input vector
        """
        self.predicted_value = -1
        started_at = ticks_us()

        self.votes = [0.00000000000, 0.00000000000]

        idx, score = self.tree0(x)
        self.votes[idx] += score
        
        idx, score = self.tree1(x)
        self.votes[idx] += score
        
        idx, score = self.tree2(x)
        self.votes[idx] += score
        
        idx, score = self.tree3(x)
        self.votes[idx] += score
        
        idx, score = self.tree4(x)
        self.votes[idx] += score
        
        idx, score = self.tree5(x)
        self.votes[idx] += score
        
        idx, score = self.tree6(x)
        self.votes[idx] += score
        
        idx, score = self.tree7(x)
        self.votes[idx] += score
        
        idx, score = self.tree8(x)
        self.votes[idx] += score
        
        idx, score = self.tree9(x)
        self.votes[idx] += score
        
        idx, score = self.tree10(x)
        self.votes[idx] += score
        
        idx, score = self.tree11(x)
        self.votes[idx] += score
        
        idx, score = self.tree12(x)
        self.votes[idx] += score
        
        idx, score = self.tree13(x)
        self.votes[idx] += score
        
        idx, score = self.tree14(x)
        self.votes[idx] += score
        
        idx, score = self.tree15(x)
        self.votes[idx] += score
        
        idx, score = self.tree16(x)
        self.votes[idx] += score
        
        idx, score = self.tree17(x)
        self.votes[idx] += score
        
        idx, score = self.tree18(x)
        self.votes[idx] += score
        
        idx, score = self.tree19(x)
        self.votes[idx] += score

        # get argmax of votes
        max_vote = max(self.votes)
        self.predicted_value = next(i for i, v in enumerate(self.votes) if v == max_vote)

        self.latency = ticks_diff(ticks_us(), started_at)
        return self.predicted_value

    def latencyInMicros(self):
        """
        Get latency in micros
        """
        return self.latency

    def latencyInMillis(self):
        """
        Get latency in millis
        """
        return self.latency // 1000

    def tree0(self, x):
        """
        Random forest's tree #0
        """
        if x[0] < 69.0:
            return 0, 0.47368421052631576
        else:
            if x[0] < 76.0:
                return 1, 0.5263157894736842
            else:
                return 0, 0.47368421052631576

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[0] < 69.0:
            return 0, 0.49122807017543857
        else:
            if x[1] < 29.0:
                return 1, 0.5087719298245614
            else:
                return 0, 0.49122807017543857

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[1] < 29.5:
            return 1, 0.43859649122807015
        else:
            return 0, 0.5614035087719298

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[0] < 69.0:
            return 0, 0.5263157894736842
        else:
            if x[0] < 76.0:
                return 1, 0.47368421052631576
            else:
                return 0, 0.5263157894736842

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[0] < 69.0:
            return 0, 0.38596491228070173
        else:
            if x[0] < 76.0:
                return 1, 0.6140350877192983
            else:
                return 0, 0.38596491228070173

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[1] < 29.0:
            return 1, 0.45614035087719296
        else:
            return 0, 0.543859649122807

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[0] < 69.0:
            return 0, 0.5964912280701754
        else:
            if x[1] < 29.5:
                return 1, 0.40350877192982454
            else:
                return 0, 0.5964912280701754

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[1] < 29.5:
            return 1, 0.47368421052631576
        else:
            return 0, 0.5263157894736842

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[0] < 76.0:
            if x[1] < 30.0:
                return 1, 0.6666666666666666
            else:
                return 0, 0.3333333333333333
        else:
            return 0, 0.3333333333333333

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[0] < 69.0:
            return 0, 0.45614035087719296
        else:
            if x[0] < 76.0:
                return 1, 0.543859649122807
            else:
                return 0, 0.45614035087719296

    def tree10(self, x):
        """
        Random forest's tree #10
        """
        if x[1] < 29.0:
            return 1, 0.543859649122807
        else:
            return 0, 0.45614035087719296

    def tree11(self, x):
        """
        Random forest's tree #11
        """
        if x[0] < 76.0:
            if x[0] < 69.0:
                return 0, 0.40350877192982454
            else:
                return 1, 0.5964912280701754
        else:
            return 0, 0.40350877192982454

    def tree12(self, x):
        """
        Random forest's tree #12
        """
        if x[0] < 76.0:
            if x[1] < 30.0:
                return 1, 0.5263157894736842
            else:
                return 0, 0.47368421052631576
        else:
            return 0, 0.47368421052631576

    def tree13(self, x):
        """
        Random forest's tree #13
        """
        if x[0] < 76.0:
            if x[1] < 30.0:
                return 1, 0.543859649122807
            else:
                return 0, 0.45614035087719296
        else:
            return 0, 0.45614035087719296

    def tree14(self, x):
        """
        Random forest's tree #14
        """
        if x[1] < 29.5:
            return 1, 0.5087719298245614
        else:
            return 0, 0.49122807017543857

    def tree15(self, x):
        """
        Random forest's tree #15
        """
        if x[0] < 69.0:
            return 0, 0.543859649122807
        else:
            if x[1] < 29.5:
                return 1, 0.45614035087719296
            else:
                return 0, 0.543859649122807

    def tree16(self, x):
        """
        Random forest's tree #16
        """
        if x[1] < 29.0:
            return 1, 0.5087719298245614
        else:
            return 0, 0.49122807017543857

    def tree17(self, x):
        """
        Random forest's tree #17
        """
        if x[0] < 69.0:
            return 0, 0.43859649122807015
        else:
            if x[0] < 76.0:
                return 1, 0.5614035087719298
            else:
                return 0, 0.43859649122807015

    def tree18(self, x):
        """
        Random forest's tree #18
        """
        if x[1] < 30.0:
            return 1, 0.5614035087719298
        else:
            return 0, 0.43859649122807015

    def tree19(self, x):
        """
        Random forest's tree #19
        """
        if x[0] < 69.0:
            return 0, 0.42105263157894735
        else:
            if x[1] < 29.0:
                return 1, 0.5789473684210527
            else:
                return 0, 0.42105263157894735