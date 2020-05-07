dict2 = {
"gebs_key" : ["gaussianelimination", "gaussianbackwardsubstitution", "gebs",
              "gausianpartialpivoting", "partialpivoting", "gaussianscaledpivoting",
              "scaledpivoting", "gepartialpivoting", "gescaledpivoting"],
"fact_key" : ["lufactorization", "lu", "cholesky", "choleskyfactorization",
              "ldlt", "ldltfactorization"],
"crout_key" : ["crout", "croutfactorization", "croutsolution"],
"iter_key" : ["iterativemethods", "gaussseidel", "jacobi", "sor", "gauss_seidel",
              "gauss-seidel", "jacobiiterativemethod"],
"mult_key" : ["matrixmultiplication", "matmul", "matrixproduct"],
"det_key" : ["det", "determinant"]

}

def help(kw = " "):
  print("Method located in NApy.matrix_methods \\n")
  if((kw.lower()).replace(" ", "") in dict2["gebs_key"]):
    Notes = '''
    Gaussian Elimination - Backward Substitution
      function name: gaussian_elim

      Inputs: n: Dimension of matrix A
              A: Matrix A (preferably written as a numpy array)
              b: vector b (preferably written as a numpy array)
              ver: Ternary input
                  Default ver = 0: Ordinary Gaussian Elimination
                          ver = 1: Gaussian Elimination with partial pivoting
                          ver = 2: Gaussian Elimination with scaled pivoting

      Outputs: x: solution vector (returned as a numpy array)
    '''
    print(Notes)


  if((kw.lower()).replace(" ", "") in dict2["fact_key"]):
    Notes = '''
    Factorization methods:
      function name: matrix_fact

      Inputs: n: Dimension of matrix A
              A: Matrix A (preferably written as a numpy array)
              type:
                Default type = "lu": LU factorization
                        type = "ldlt": LDLt factorization
                        type = "cholesky": Cholesky factorization
      Outputs:
          type = "lu": [L, U]
          type = "cholesky": L
          type = "ldlt": [L, D]
    '''
    print(Notes)

  if((kw.lower()).replace(" ", "") in dict2["crout_key"]):
    Notes = '''
    Crout mathod
      function name: crout

      Inputs: n: Dimension of matrix A
              A: Matrix A (preferably written as a numpy array)
              b: vector b (preferably written as a numpy array)

      Outputs: x (as a numpy array. Solution to Ax = B)
    '''
    print(Notes)

  if((kw.lower()).replace(" ", "") in dict2["iter_key"]):
    Notes =  '''
    Iterative matrix methods
      function name: mat_iter

      Inputs: A: Matrix A (preferably written as a numpy array)
              b: vector b (preferably written as a numpy array)
              xo: initial x value (preferably written as a numpy array)
              N: maximum number of iteration
              w: default w = 0: For any method
                         w = any number: for SOR method
              type:
                type = "jacobi": Jacobi iterative method
                type = "gauss-seidel": Gauss Seidel iterative method
                type = "sor": SOR iterative method
    '''
    print(Notes)

  if((kw.lower()).replace(" ", "") in dict2["mult_key"]):
    Notes = '''
    Matrix multiplication
      function name: Matmul

      Inputs: A: Matrix A (preferably written as a numpy array)
              B: Matrix B (preferably written as a numpy array)

      Outputs: C = AB the product matrix (as a numpy array)
    '''
    print(Notes)

  if((kw.lower()).replace(" ", "") in dict2["det_key"]):
    Notes = '''
    Determinant
      function name: determinant

      Inputs: A: Matrix A (preferably written as a numpy array)

      Outputs: det(A) the determinant of A
    '''
    print(Notes)
  return 0
