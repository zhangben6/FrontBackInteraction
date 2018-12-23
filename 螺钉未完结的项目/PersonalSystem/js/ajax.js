/**
 *??????????? ????????
 * @param method ????????
 * @param url ???????
 * @param data ?????????
 * @param success ??????????????????????????? ?????????????
 * return undefined
 */
function ajax(options) {
  // ??method????  ????get
  var method = options.method || 'get';
  //  ????????
  var xhr = null;
  try {
    xhr = new XMLHttpRequest();
  } catch (e) {
    xhr = new ActiveXObject('Microsoft.XMLHTTP');
  }
  if (method === 'get') {
    xhr.open('get', options.url + "?" + options.data, true);
    xhr.send();
  } else if (method === 'post') {

    xhr.open('post', options.url, true);
    xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    xhr.send(options.data);
  } else {
    console.log("??????????")
  }
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var arr = JSON.parse(xhr.responseText);
      /**
       * success ==  function(data){
          var oUl = document.getElementById('ul1');
          //  ????li ????????li?????
          for(var i=0;i < data.length; i++){
            var oLi = document.createElement('li');
            oLi.innerHTML = arr[i].title;
            oUl.appendChild(oLi);
          }
        }
       */
      options.success && options.success(arr);

      // function aa(data){}
      //
      // aa(arr)
    }

  }
}
