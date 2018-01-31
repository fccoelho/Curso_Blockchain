import {Template} from 'meteor/templating';
import {ReactiveVar} from 'meteor/reactive-var';

import './main.html';
var MyContract = web3.eth.contract([{
        "constant": true,
        "inputs": [{"name": "", "type": "address"}],
        "name": "turma",
        "outputs": [{"name": "matriculado", "type": "bool"}, {"name": "presencas", "type": "uint256"}],
        "payable": false,
        "type": "function"
    }, {
        "constant": false,
        "inputs": [],
        "name": "assinaPresenca",
        "outputs": [],
        "payable": false,
        "type": "function"
    }, {
        "constant": false,
        "inputs": [{"name": "aluno", "type": "address"}],
        "name": "registraAluno",
        "outputs": [],
        "payable": false,
        "type": "function"
    }, {"inputs": [], "payable": false, "type": "constructor"}]
);

var ListaDePresenca = MyContract.at('0xd05593da2716a8d60ed0a4354ce0f38b3f900025');
var turma = ListaDePresenca.turma;

Template.presenca.onCreated(function presencaOnCreated() {
    // counter starts at 0
    this.counter = new ReactiveVar(0);
    console.log(web3);
});

Template.presenca.helpers({
    counter() {
        return Template.instance().counter.get();
    }

});

Template.presenca.events({
    'click button'(event, instance) {
        // increment the counter when button is clicked
        instance.counter.set(instance.counter.get() + 1);
    }
});

Template.turma.onCreated(function turmaOnCreated() {
    this.lista = new ReactiveVar(turma);
});

Template.turma.helpers({
    lista(){
        return Template.instance().lista.get();
    }
});
Template.turma.events({});

Template.matricula.onCreated(function matriculaOnCreated() {
    //lists registered students by querying the contract
});

Template.login.onCreated(function loginOnCreated() {
    this.dados = new ReactiveVar('Nada')
});
Template.login.helpers({
    dados(){
        return Template.instance().dados.get();
    }
});
Template.login.events({
    'submit login-form'(event){
        // Prevent default browser form submit
        event.preventDefault();

        // Get value from form element
        const target = event.target;
        const endereco = target.addr.value;
        var ficha = turma(endereco);
        const matriculado = ficha.matriculado;
        const presencas = ficha.presencas;
        this.dados.set("Matriculado:" );//+ matriculado.toString() + "Presenças:" + presencas.toString())
    }
});
