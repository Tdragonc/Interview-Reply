    function createMathOperation(operator, defaultValue) {
      return function(value) {
        return function(other) {
         var result;
        if (value === undefined && other === undefined) {
          return defaultValue;
        }
        if (value !== undefined) {
          result = value;
        }
        if (other !== undefined) {
          if (result === undefined) {
            return other;
          }
          if (typeof value == 'string' || typeof other == 'string') {
            value = baseToString(value);
            other = baseToString(other);
          } else {
            value = baseToNumber(value);
            other = baseToNumber(other);
          }
          result = operator(value, other);
        }
        return result;
        };
      };
    }
    
    var addin = createMathOperation(function(augend) {
      return function(addend) {
        return augend + addend
      }
    }, 0);

_.addin(2)(3)