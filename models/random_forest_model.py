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
        if x[1] < -0.03877637255936861:
            return 0, 0.4488479262672811
        else:
            if x[2] < -1.800160527229309:
                if x[1] < 0.7422173321247101:
                    if x[0] < -0.03557312488555908:
                        return 0, 0.4488479262672811
                    else:
                        return 1, 0.5511520737327189
                else:
                    return 1, 0.5511520737327189
            else:
                if x[0] < -0.2605021595954895:
                    return 0, 0.4488479262672811
                else:
                    return 1, 0.5511520737327189

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[1] < -0.03926698584109545:
            return 0, 0.4184331797235023
        else:
            if x[2] < -1.8003764152526855:
                if x[0] < -0.23765304684638977:
                    return 0, 0.4184331797235023
                else:
                    return 1, 0.5815668202764976
            else:
                if x[0] < -0.27608148753643036:
                    return 0, 0.4184331797235023
                else:
                    return 1, 0.5815668202764976

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[1] < 0.06716442853212357:
            if x[0] < 0.21570314466953278:
                return 0, 0.4700460829493088
            else:
                return 1, 0.5299539170506913
        else:
            return 1, 0.5299539170506913

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[1] < 0.11055101454257965:
            if x[0] < 0.2191341668367386:
                return 0, 0.471889400921659
            else:
                return 1, 0.528110599078341
        else:
            return 1, 0.528110599078341

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[2] < -0.5535843670368195:
            if x[2] < -1.4888978600502014:
                if x[2] < -1.7791837453842163:
                    if x[0] < -0.11627534031867981:
                        return 0, 0.44055299539170506
                    else:
                        return 1, 0.5594470046082949
                else:
                    if x[2] < -1.5533748865127563:
                        return 0, 0.44055299539170506
                    else:
                        if x[1] < 0.022416681051254272:
                            return 0, 0.44055299539170506
                        else:
                            return 1, 0.5594470046082949
            else:
                if x[1] < -0.12604472134262323:
                    return 0, 0.44055299539170506
                else:
                    return 1, 0.5594470046082949
        else:
            if x[0] < -0.02535596489906311:
                return 0, 0.44055299539170506
            else:
                return 1, 0.5594470046082949

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[1] < 0.07577582448720932:
            return 0, 0.44423963133640554
        else:
            return 1, 0.5557603686635945

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[1] < -0.03877637255936861:
            return 0, 0.45622119815668205
        else:
            if x[2] < -0.1367291733622551:
                if x[1] < 0.11850961297750473:
                    if x[1] < 0.047278827987611294:
                        return 1, 0.543778801843318
                    else:
                        return 0, 0.45622119815668205
                else:
                    return 1, 0.543778801843318
            else:
                return 1, 0.543778801843318

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[2] < -0.8879128098487854:
            if x[2] < -1.5533748865127563:
                if x[1] < -0.010358437895774841:
                    return 0, 0.4525345622119816
                else:
                    return 1, 0.5474654377880185
            else:
                if x[2] < -1.5515174269676208:
                    return 1, 0.5474654377880185
                else:
                    if x[1] < -0.03710433840751648:
                        return 0, 0.4525345622119816
                    else:
                        return 1, 0.5474654377880185
        else:
            if x[1] < 0.07577582448720932:
                if x[2] < 1.0065221190452576:
                    return 0, 0.4525345622119816
                else:
                    if x[0] < 0.054059624671936035:
                        return 0, 0.4525345622119816
                    else:
                        return 1, 0.5474654377880185
            else:
                return 1, 0.5474654377880185

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[1] < -0.03877637255936861:
            return 0, 0.45714285714285713
        else:
            if x[0] < -0.33459626138210297:
                return 0, 0.45714285714285713
            else:
                return 1, 0.5428571428571428

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[0] < -0.04093529284000397:
            return 0, 0.4258064516129032
        else:
            return 1, 0.5741935483870968

    def tree10(self, x):
        """
        Random forest's tree #10
        """
        if x[1] < -0.12474061641842127:
            return 0, 0.41751152073732717
        else:
            if x[2] < -1.8003764152526855:
                if x[0] < -0.23765304684638977:
                    return 0, 0.41751152073732717
                else:
                    return 1, 0.5824884792626728
            else:
                if x[2] < 0.45094460248947144:
                    if x[0] < -0.2178245186805725:
                        return 0, 0.41751152073732717
                    else:
                        return 1, 0.5824884792626728
                else:
                    return 1, 0.5824884792626728

    def tree11(self, x):
        """
        Random forest's tree #11
        """
        if x[1] < 0.07577582448720932:
            return 0, 0.4313364055299539
        else:
            if x[1] < 0.6753930151462555:
                if x[1] < 0.6731212139129639:
                    return 1, 0.5686635944700461
                else:
                    return 0, 0.4313364055299539
            else:
                return 1, 0.5686635944700461

    def tree12(self, x):
        """
        Random forest's tree #12
        """
        if x[2] < -0.8700530529022217:
            if x[0] < -0.08186832070350647:
                return 0, 0.4258064516129032
            else:
                return 1, 0.5741935483870968
        else:
            if x[1] < 0.07577582448720932:
                if x[2] < 1.0065221190452576:
                    return 0, 0.4258064516129032
                else:
                    if x[0] < 0.10223373770713806:
                        return 0, 0.4258064516129032
                    else:
                        return 1, 0.5741935483870968
            else:
                return 1, 0.5741935483870968

    def tree13(self, x):
        """
        Random forest's tree #13
        """
        if x[0] < 0.04262837767601013:
            return 0, 0.45622119815668205
        else:
            return 1, 0.543778801843318

    def tree14(self, x):
        """
        Random forest's tree #14
        """
        if x[0] < 0.05820770561695099:
            return 0, 0.4488479262672811
        else:
            return 1, 0.5511520737327189

    def tree15(self, x):
        """
        Random forest's tree #15
        """
        if x[1] < 0.07577582448720932:
            return 0, 0.45069124423963136
        else:
            return 1, 0.5493087557603686

    def tree16(self, x):
        """
        Random forest's tree #16
        """
        if x[1] < -0.12604472134262323:
            return 0, 0.44516129032258067
        else:
            if x[1] < 0.07577582448720932:
                if x[0] < -0.10300672054290771:
                    return 0, 0.44516129032258067
                else:
                    return 1, 0.5548387096774193
            else:
                if x[1] < 0.6791163682937622:
                    if x[0] < -0.33459626138210297:
                        return 0, 0.44516129032258067
                    else:
                        return 1, 0.5548387096774193
                else:
                    return 1, 0.5548387096774193

    def tree17(self, x):
        """
        Random forest's tree #17
        """
        if x[1] < 0.06716442853212357:
            if x[1] < -0.03098428063094616:
                return 0, 0.45069124423963136
            else:
                if x[1] < 0.04645952396094799:
                    return 1, 0.5493087557603686
                else:
                    return 0, 0.45069124423963136
        else:
            if x[1] < 0.6750974655151367:
                if x[1] < 0.6731212139129639:
                    return 1, 0.5493087557603686
                else:
                    return 0, 0.45069124423963136
            else:
                return 1, 0.5493087557603686

    def tree18(self, x):
        """
        Random forest's tree #18
        """
        if x[1] < 0.09138849377632141:
            return 0, 0.4359447004608295
        else:
            return 1, 0.5640552995391706

    def tree19(self, x):
        """
        Random forest's tree #19
        """
        if x[1] < 0.09999988973140717:
            return 0, 0.4433179723502304
        else:
            return 1, 0.5566820276497696