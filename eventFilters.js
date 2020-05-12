module.exports.rules = () => {
  const res = [];
  if (process.env.PREFIX) {
    res.push({ prefix: process.env.PREFIX });
  }
  if (process.env.SUFFIX) {
    res.push({ suffix: process.env.SUFFIX });
  }
  return res;
};
