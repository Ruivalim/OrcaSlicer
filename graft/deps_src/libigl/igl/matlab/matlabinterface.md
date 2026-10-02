# deps_src/libigl/igl/matlab/matlabinterface.h

- mlinit · function · L43-L43 — IGL_INLINE void mlinit(Engine** engine);
- mlclose · function · L48-L48 — IGL_INLINE void mlclose(Engine** engine);
- mlsetmatrix · function · L55-L55 — IGL_INLINE void mlsetmatrix(Engine** engine, std::string name, const Eigen::MatrixXd& M);
- mlsetmatrix · function · L58-L58 — IGL_INLINE void mlsetmatrix(Engine** engine, std::string name, const Eigen::MatrixXf& M);
- mlsetmatrix · function · L61-L61 — IGL_INLINE void mlsetmatrix(Engine** engine, std::string name, const Eigen::MatrixXi& M);
- mlsetmatrix · function · L64-L64 — IGL_INLINE void mlsetmatrix(Engine** mlengine, std::string name, const Eigen::Matrix<unsigned int, Eigen::Dynamic, Eigen::Dynamic >& M);
- mlsetmatrix · function · L67-L67 — IGL_INLINE void mlsetmatrix(Engine** mlengine, std::string name, const Eigen::SparseMatrix<double>& M);
- mlgetmatrix · function · L74-L74 — IGL_INLINE void mlgetmatrix(Engine** engine, std::string name, Eigen::MatrixXd& M);
- mlgetmatrix · function · L77-L77 — IGL_INLINE void mlgetmatrix(Engine** engine, std::string name, Eigen::MatrixXf& M);
- mlgetmatrix · function · L80-L80 — IGL_INLINE void mlgetmatrix(Engine** engine, std::string name, Eigen::MatrixXi& M);
- mlgetmatrix · function · L83-L83 — IGL_INLINE void mlgetmatrix(Engine** mlengine, std::string name, Eigen::Matrix<unsigned int, Eigen::Dynamic, Eigen::Dynamic >& M);
- mlsetscalar · function · L90-L90 — IGL_INLINE void mlsetscalar(Engine** engine, std::string name, double s);
- mleval · function · L101-L101 — IGL_INLINE std::string mleval(Engine** engine, std::string code);
