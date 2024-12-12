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
        if x[0] < 0.5778884589672089:
            if x[0] < 0.013183309230953455:
                if x[1] < -0.3414386659860611:
                    return 1, 0.49122807017543857
                else:
                    return 0, 0.5087719298245614
            else:
                if x[1] < 0.4062802791595459:
                    return 1, 0.49122807017543857
                else:
                    return 0, 0.5087719298245614
        else:
            return 0, 0.5087719298245614

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[0] < 0.560370534658432:
            if x[2] < 0.1470545269548893:
                if x[2] < -0.8767907023429871:
                    if x[2] < -1.2702441215515137:
                        if x[1] < -0.27973921597003937:
                            return 1, 0.40350877192982454
                        else:
                            return 0, 0.5964912280701754
                    else:
                        return 1, 0.40350877192982454
                else:
                    return 0, 0.5964912280701754
            else:
                if x[1] < -0.18711863458156586:
                    return 1, 0.40350877192982454
                else:
                    return 0, 0.5964912280701754
        else:
            return 0, 0.5964912280701754

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[1] < -0.25174323469400406:
            return 1, 0.5614035087719298
        else:
            return 0, 0.43859649122807015

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[1] < -0.25174323469400406:
            return 1, 0.3508771929824561
        else:
            return 0, 0.6491228070175439

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[2] < -0.9505643546581268:
            if x[1] < -0.2093098908662796:
                return 1, 0.5263157894736842
            else:
                return 0, 0.47368421052631576
        else:
            if x[1] < -0.27056556940078735:
                return 1, 0.5263157894736842
            else:
                return 0, 0.47368421052631576

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[1] < -0.25174323469400406:
            return 1, 0.5263157894736842
        else:
            return 0, 0.47368421052631576

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[1] < -0.2757159546017647:
            return 1, 0.5263157894736842
        else:
            return 0, 0.47368421052631576

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[1] < -0.25174323469400406:
            return 1, 0.5087719298245614
        else:
            return 0, 0.49122807017543857

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[0] < 0.6003620624542236:
            if x[1] < -0.15954185277223587:
                return 1, 0.5614035087719298
            else:
                return 0, 0.43859649122807015
        else:
            return 0, 0.43859649122807015

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[1] < -0.25174323469400406:
            return 1, 0.49122807017543857
        else:
            return 0, 0.5087719298245614

    def tree10(self, x):
        """
        Random forest's tree #10
        """
        if x[2] < 0.3011793792247772:
            if x[1] < -0.24313569068908691:
                return 1, 0.40350877192982454
            else:
                return 0, 0.5964912280701754
        else:
            if x[1] < -0.22159988433122635:
                return 1, 0.40350877192982454
            else:
                return 0, 0.5964912280701754

    def tree11(self, x):
        """
        Random forest's tree #11
        """
        if x[2] < 1.5865886807441711:
            if x[0] < 0.11696084588766098:
                if x[1] < -0.36526448279619217:
                    return 1, 0.38596491228070173
                else:
                    return 0, 0.6140350877192983
            else:
                if x[2] < 0.8090915083885193:
                    if x[0] < 0.5892453640699387:
                        if x[2] < 0.5964679419994354:
                            return 1, 0.38596491228070173
                        else:
                            if x[1] < 0.1620507836341858:
                                return 1, 0.38596491228070173
                            else:
                                return 0, 0.6140350877192983
                    else:
                        return 0, 0.6140350877192983
                else:
                    return 0, 0.6140350877192983
        else:
            return 1, 0.38596491228070173

    def tree12(self, x):
        """
        Random forest's tree #12
        """
        if x[2] < -0.9307751059532166:
            if x[0] < -1.5321365371346474:
                return 0, 0.543859649122807
            else:
                if x[2] < -1.2950095534324646:
                    if x[0] < 0.5174444690346718:
                        return 1, 0.45614035087719296
                    else:
                        return 0, 0.543859649122807
                else:
                    return 1, 0.45614035087719296
        else:
            if x[0] < 0.5276211053133011:
                if x[1] < -0.21094445139169693:
                    return 1, 0.45614035087719296
                else:
                    return 0, 0.543859649122807
            else:
                return 0, 0.543859649122807

    def tree13(self, x):
        """
        Random forest's tree #13
        """
        if x[2] < -0.9307751059532166:
            if x[2] < -1.75633305311203:
                return 0, 0.47368421052631576
            else:
                return 1, 0.5263157894736842
        else:
            if x[2] < 0.22409099340438843:
                if x[0] < 0.12992827594280243:
                    if x[1] < -0.29927365481853485:
                        return 1, 0.5263157894736842
                    else:
                        return 0, 0.47368421052631576
                else:
                    return 0, 0.47368421052631576
            else:
                if x[1] < -0.3031458333134651:
                    return 1, 0.5263157894736842
                else:
                    return 0, 0.47368421052631576

    def tree14(self, x):
        """
        Random forest's tree #14
        """
        if x[2] < 0.2189965769648552:
            if x[1] < -0.3269881308078766:
                return 1, 0.3157894736842105
            else:
                return 0, 0.6842105263157895
        else:
            if x[1] < -0.21094445139169693:
                return 1, 0.3157894736842105
            else:
                return 0, 0.6842105263157895

    def tree15(self, x):
        """
        Random forest's tree #15
        """
        if x[1] < -0.25174323469400406:
            return 1, 0.543859649122807
        else:
            return 0, 0.45614035087719296

    def tree16(self, x):
        """
        Random forest's tree #16
        """
        if x[2] < 0.216395765542984:
            if x[0] < 0.6346893310546875:
                if x[1] < -0.12387003004550934:
                    return 1, 0.543859649122807
                else:
                    return 0, 0.45614035087719296
            else:
                return 0, 0.45614035087719296
        else:
            if x[0] < 0.02402062388136983:
                return 0, 0.45614035087719296
            else:
                if x[2] < 1.3742717504501343:
                    if x[1] < -0.31380126625299454:
                        return 1, 0.543859649122807
                    else:
                        return 0, 0.45614035087719296
                else:
                    if x[1] < -0.14253529906272888:
                        return 1, 0.543859649122807
                    else:
                        return 0, 0.45614035087719296

    def tree17(self, x):
        """
        Random forest's tree #17
        """
        if x[1] < -0.25174323469400406:
            return 1, 0.5263157894736842
        else:
            return 0, 0.47368421052631576

    def tree18(self, x):
        """
        Random forest's tree #18
        """
        if x[0] < 0.5703441053628922:
            if x[2] < -0.8767907023429871:
                if x[2] < -1.2702441215515137:
                    if x[1] < 0.3124394416809082:
                        return 1, 0.40350877192982454
                    else:
                        return 0, 0.5964912280701754
                else:
                    return 1, 0.40350877192982454
            else:
                if x[1] < -0.30398673564195633:
                    return 1, 0.40350877192982454
                else:
                    return 0, 0.5964912280701754
        else:
            return 0, 0.5964912280701754

    def tree19(self, x):
        """
        Random forest's tree #19
        """
        if x[2] < 0.5797109007835388:
            if x[0] < 0.5928177088499069:
                if x[2] < 0.2189965769648552:
                    if x[0] < 0.11173573136329651:
                        return 0, 0.3684210526315789
                    else:
                        return 1, 0.631578947368421
                else:
                    return 1, 0.631578947368421
            else:
                return 0, 0.3684210526315789
        else:
            if x[1] < -0.3031458333134651:
                return 1, 0.631578947368421
            else:
                return 0, 0.3684210526315789