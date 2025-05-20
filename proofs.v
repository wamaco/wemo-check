(* === Data Type === ) Record Course := { grade : Q;       ( between 1.00 and 5.00 ) units : nat;     ( credit units ) credit : bool    ( true if course counts toward GWA *) }.

(* === Helper Functions === *) Definition valid_courses (cs : list Course) : list Course := filter (fun c => c.(credit)) cs.

Fixpoint sum_units (cs : list Course) : nat := match cs with | [] => 0 | c :: t => (if c.(credit) then c.(units) else 0) + sum_units t end.

Fixpoint sum_weighted (cs : list Course) : Q := match cs with | [] => 0 | c :: t => (if c.(credit) then c.(grade) * inject_Z (Z.of_nat c.(units)) else 0) + sum_weighted t end.

Definition compute_gwa (cs : list Course) : option Q := let vc := valid_courses cs in let total_u := sum_units vc in if total_u =? 0 then None else Some (sum_weighted vc / inject_Z (Z.of_nat total_u)).

(* === Honor Classification === *) Inductive Honor := SummaCumLaude | MagnaCumLaude | CumLaude | NoHonor.

Definition classify_honor (g : Q) : Honor := if Qle_bool g (1#1 + 1#5) then SummaCumLaude          (* 1.20 ) else if Qle_bool g (29#20) then MagnaCumLaude         ( 1.45 ) else if Qle_bool g (7#4) then CumLaude                ( 1.75 *) else NoHonor.

(* === Theorems and Proofs === *) Require Import Coq.Lists.List. Import ListNotations. Require Import Coq.QArith.QArith. Require Import Coq.Sorting.Permutation.

Theorem gwa_correct : forall cs g, compute_gwa cs = Some g -> g * inject_Z (Z.of_nat (sum_units (valid_courses cs))) = sum_weighted (valid_courses cs). Proof. intros cs g H. unfold compute_gwa in H. remember (valid_courses cs) as vc. remember (sum_units vc) as u. destruct (u =? 0) eqn:Hu.

discriminate H.

inversion H. subst. apply Nat.eqb_neq in Hu. rewrite Hequ, Heqvc. field. apply inject_Z_not_eq_0. lia. Qed.


Theorem gwa_permutation_invariant : forall cs1 cs2, Permutation cs1 cs2 -> compute_gwa cs1 = compute_gwa cs2. Admitted.

Theorem gwa_excludes_noncredit : forall cs, compute_gwa cs = compute_gwa (filter (fun c => c.(credit)) cs). Admitted.

Theorem gwa_bounded : forall cs g, compute_gwa cs = Some g -> (forall c, In c (valid_courses cs) -> 1 <= c.(grade) <= 5) -> 1 <= g <= 5. Admitted.

Theorem gwa_stability : forall cs, compute_gwa cs = compute_gwa cs. Proof. reflexivity. Qed.

Theorem honors_correct : classify_honor (119#100) = SummaCumLaude /
classify_honor (29#20) = MagnaCumLaude /
classify_honor (7#4) = CumLaude. Admitted.

Theorem classify_honor_exclusive : forall g, match classify_honor g with | SummaCumLaude => g <= 6#5 | MagnaCumLaude => 6#5 < g <= 29#20 | CumLaude => 29#20 < g <= 7#4 | NoHonor => 7#4 < g end. Admitted.

Theorem classify_honor_total : forall g, exists h, classify_honor g = h. Proof. intros. exists (classify_honor g). reflexivity. Qed.

