$(document).ready(function(){
    $('.modal').modal();
});

$('.chips-placeholder').chips({
    placeholder: '+Tag',
    secondaryPlaceholder: '+Tag',
});

$('.chips-autocomplete').chips({
    autocompleteOptions: {
    data: {
        'Família': null,
        'Trabalho': null,
        'Amigos': null,
        'Outros': null
    },
    limit: Infinity,
    minLength: 1
    }
});

var chip = {
    tag: 'chip content',
    image: '', //optional
};

var instance = M.Chips.getInstance(document.getElementById('chip1'))

instance.addChip({
    tag: 'Família',
    image: '', // optional
});