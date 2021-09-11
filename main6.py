import numpy as np

tableau1=np.array([[0,1,2]])
tableau2=np.array([[2,1,0]])
m_cov=np.cov(tableau1,tableau2)
print(m_cov)