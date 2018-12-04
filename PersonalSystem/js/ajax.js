/**
 *�����Ĭ�ϲ��� �Ϳ��Բ���
 * @param method ����ķ���
 * @param url ����ĵ�ַ
 * @param data ���͵�����
 * @param success ��������ɹ��Ժ���Ҫ�����ҵ���߼� ����һ��������
 * return undefined
 */
function ajax(options) {
  // ��methodĬ��ֵ  Ĭ��Ϊget
  var method = options.method || 'get';
  //  ��������
  var xhr = null;
  try {
    xhr = new XMLHttpRequest();
  } catch (e) {
    xhr = new ActiveXObject('Microsoft.XMLHTTP');
  }
  if (method === 'get') {
    xhr.open('get', options.url + "?" + options.data, true);
    xhr.send();
  } else if (method.toLowerCase() === 'post') {

    xhr.open('post', options.url, true);
    xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    xhr.send(options.data);
  } else {
    console.log("����ʽ����ȷ")
  }
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var arr = JSON.parse(xhr.responseText);
      /**
       * success ==  function(data){
          var oUl = document.getElementById('ul1');
          //  ����li �����ݷŵ�li����ȥ
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
alert(111)