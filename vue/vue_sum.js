new Vue({
    el: '#some_element'
})

Vue.compnent('my-compnent', {
    data()
})

Vue.component('child', {
    props: ['message'],
    template: '<span>{{message}}</span>'
})
<div>
    <input type="text" v-model='parent-msg'/>
    <br/>
    <child :message='parent-msg'></child>
</div>

<comp some-prop='1'></comp>
<comp :some-prop='1'></comp>

<my-component v-on:click.native='doTheThing'></my-component>

var parent = new Vue({
    el: '#parent'
})
var child = parent.$refs.profile

手动按f5刷新页面，这个时候会重新构建vue实例，而又没有重新登录，所以vuex里面的东西会清空，
所以将登录后的数据存放在sessionStroage中，在刷新页面，重新构建vue实例的时候，会有判断

